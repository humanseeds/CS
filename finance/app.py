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
    # Display HTML table with the following. use lookup, SELECT GROUP BY HAVING SUM or WHERE
    # looping templates
        # python- return render_template("hello.html",
            # contact=[{"name":"  ", "  ": "  "},
                        # {"name": "  ", "  ": "  "}]
         # jinja- {% for contact in contacts %}
                    # <p>{{ contact.name}} live in {{contact.house}}</p>
                # {% endfor %}
            # all stocks owned
            # number of shares per stock
            # current price of each stock
         # total value of each holding
    # Display users cash balance
    # display total value of stocks and cash together

    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # When request via GET, display buy stock form
    if request.method == "GET":
        return render_template("buy.html")

    # require stocks symbol implemented name as symbol for lookup or return an apology
    symbol = request.form.get("symbol")
	input_shares = request.form.get("shares")


    # require user input number of shares in textfield name is shares or render apology if not positive int
	if not symbol:
            return apology("Must Provide a Valid Symbol")

	if not input_shares or not input_shares.isdigit() or int(input_shares) <= 0:
		return apology("Invalid Amount of Shares")

    # convert amount of shares to an integer
    shares = int(input_shares)

    # return user to homescreen
	Return render_template("home.html")

    # call the lookup function to find the stock price
    stock = lookup(symbol.upper())
    if not stock:
		return apology("Symbol Not Found")


    #calculate purchase
	price = quote["price"]
    cost = shares * price


    user_cash = db.execute("SELECT cash FROM user WHERE id = :user_id", user_id=session,[user_id][0]["cash"]
    if user_cash < cost:
		return.apology("Insufficient Funds")

    # update users table
	db.execute("UPDATE users SET cash = cash - :cost WHER id = :user_id",
		cost=cost,
        user_id=session["user_id"])

    # add purchase to history table
	db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (":user_id, :symbol, :shares, :price)",
		user_id= session["user_id"],
        symbol=symbol,
        shares=shares,
        price=prices
        )

    # return user to homescreen
	return redirect("/")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # display html table with history of all transactioins. one row per buy or sell
    # each row contains stock name, bought or sold, purchase of sale price, number of shares and date and time
    #alter table for buy to minimize redundancies
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
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
    # when request via GET, display stock quote
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Must Give Valid Symbol")

        quote = lookup(symbol)

        if not quote:
            return apology("Invalid Symbol")

        return render_template("quote.html", quote=quote)


    return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Input Valid Username")
        if not password:
            return apology("Input Valid Password")
        if not confirmation:
            return apology("Must Confirm Password")

        if password != confirmation:
            return apology("Passwords Must Match")

        hash = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES(?,?)", username, hash)
        except:
            return apology("Username Already Exists")


        session["user_id"] = rows[0]["id"]


        return redirect("/")


    return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # When requested via GET, display form to sell stock
        # display form implemented as select
        # name is symbol
        #render apology user doesnt ownt the stock or selects the wrong stock
        # require number of shares as text field whose name is shares. render apology if integer is negative
    #submit via POST to SELL
    # when submitted via POST, check for errors and sell specified number of shares and updates users cash

    # redirect to homepage upoin completion
    return apology("TODO")


# NEW FEATURE
    # create new features not listed i.e change password, add cash to account,
    # or add more stocks or shares already owned viaw index
