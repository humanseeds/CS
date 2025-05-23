import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # get logged in users data
    user_id = session["user_id"]

    # search the database for user's stock portfolio
    transactions = db.execute("""
        SELECT symbol, SUM(shares) AS total_shares
        FROM transactions
        WHERE user_id = :user_id
        GROUP BY symbol
        HAVING total_shares > 0
    """, user_id=user_id)

    # make a list to store the stock data
    stocks = []

    # Loop through transactions and find the symbols and amount of shares
    for transaction in transactions:
        symbol = transaction["symbol"]
        total_shares = transaction["total_shares"]

        # Use the lookup function to find the  real time stock name,symbol,total shares, price and value
        stock_data = lookup(symbol)
        if stock_data:
            stocks.append({
                "symbol": symbol,
                "name": stock_data["name"],
                "price": stock_data["price"],
                "total_shares": total_shares,
                "value": total_shares * stock_data["price"]
            })

    # search for the user's cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0]["cash"]

    # Calculate the total value (cash + stocks)
    total_value = cash + sum(stock["value"] for stock in stocks)

    # Render the index.html with stock data, cash, and grand total
    return render_template("index.html", stocks=stocks, cash=cash, total_value=total_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # When request via GET, display buy stock form
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        # require stocks symbol implemented name as symbol for lookup or return an apology
        symbol = request.form.get("symbol")
        input_shares = request.form.get("shares")

    # require user input number of shares in textfield name is shares or render apology if not positive int
        if not symbol:
            return apology("Must Provide a Valid Symbol")
        if not input_shares or not input_shares.isdigit() or int(input_shares) <= 0:
            return apology("Invalid Amount of Shares")

    # call the lookup function to find the stock price
        stock = lookup(symbol.upper())
        if not stock:
            return apology("Symbol Not Found")

    # calculate purchase
        price = stock["price"]
        shares = int(input_shares)
        cost = shares * price

    # determine if user has sufficient funds for the purchase order
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session["user_id"])[0]["cash"]
        if cash < cost:
            return apology("Insufficient Funds")

    # update users table
        db.execute("UPDATE users SET cash = cash - :cost WHERE id = :user_id",
                   cost=cost,
                   user_id=session["user_id"])

    # add purchase to history table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"],
                   symbol=symbol,
                   shares=shares,
                   price=price
                   )

    # Flash a message confirming the purchase order
        flash(f"Congratulations! Purchase of {shares} of {symbol} for {usd(cost)} complete")

    # return user to homescreen
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # search databse for all of users transaction and put them in decending order
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC", user_id=session["user_id"])

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # when request via post
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # search database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # make sure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # If request via GET redirect
    if request.method == "GET":
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # when request via POST, display stock quote
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # return apology if stock symbol is invalid
        if not symbol:
            return apology("Must Give Valid Symbol")

        # use lookup function to return stock symbol quote
        quote = lookup(symbol)

        # return apology if symbol is not found
        if not quote:
            return apology("Invalid Symbol")

        # format price
        quote["price"] = usd(quote["price"])

        # render the quote.html when the stock info is found
        return render_template("quote.html", quote=quote)

    # for Get request, diisplay the quote form
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # clear all existing session data
    session.clear()

    # when request via GET, user is visting the registration page
    if request.method == "GET":
        return render_template("register.html")

    # if request is POST from form submission, process registration
    if request.method == "POST":

        # retrieve data from registratioin form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # check is username,password, and confirmation are valid
        if not username:
            return apology("Input Valid Username")
        if not password:
            return apology("Input Valid Password")
        if not confirmation:
            return apology("Must Confirm Password")
        if password != confirmation:
            return apology("Passwords Must Match")
        if password != confirmation:
            return apology("Passwords Must Match")

        # check if username is already taken
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", (username,))

        # return apology if username is already taken
        if existing_user:
            return apology("Username Already Exists")

        # hash user password for security
        hash = generate_password_hash(password)

        # insert new user into sql new user table, return error if name exists
        try:
            new_user = db.execute(
                "INSERT INTO users (username, hash) VALUES(?,?)", username, hash)
        except:
            return apology("Username Already Exists")

        # store user ID session to automically log them in
        session["user_id"] = new_user

        # redirect user to home page if registration was successful
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        # Search database for available stocks to sell
        stocks = db.execute("""
            SELECT symbol, SUM(shares) AS total_shares
            FROM transactions
            WHERE user_id = :user_id
            GROUP BY symbol
            HAVING total_shares > 0
        """, user_id=session["user_id"])

        # Pass available stock to the HTML template
        return render_template("sell.html", stocks=stocks)
    # if request via post
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # check if valid symbol and amount of shares
        if not symbol:
            return apology("Must provide stock symbol")

        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("Must provide a positive amount of shares")

        # create a variable for the amount of shares user wants to sell
        shares = int(shares)

        # find how many shares of each stock the user has
        user_shares = db.execute("""
            SELECT SUM(shares) AS total_shares
            FROM transactions
            WHERE user_id = :user_id
            AND symbol = :symbol
            GROUP BY symbol
        """, user_id=session["user_id"], symbol=symbol)

        # make sure the user has enough shares to sell and the number is positive/not zero
        if not user_shares or user_shares[0]["total_shares"] < shares:
            return apology("Not enough shares for sell order")

        # make sure the user is not trying to sell more shares than they own
        if shares > user_shares[0]["total_shares"]:
            flash("You don't own enough shares to sell that amount.", "error")
            return redirect("/sell")

        # look up the price of the stock symbol selected
        stock_price = lookup(symbol)

        # Record the sale into the database
        db.execute("""
            INSERT INTO transactions(user_id, symbol, shares, price)
            VALUES (:user_id, :symbol, :shares, :price)
        """, user_id=session["user_id"], symbol=symbol, shares=-shares, price=stock_price["price"])

        # Calculate total value and update user's cash total
        total_value = shares * stock_price["price"]
        db.execute("""
            UPDATE users
            SET cash = cash + :total_value
            WHERE id = :user_id
        """, total_value=total_value, user_id=session["user_id"])

        flash(
            f"Congratulations! Your sale of {shares} of {symbol} for {usd(total_value)} is complete")
        return redirect("/")
