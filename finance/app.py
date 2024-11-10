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
        #python- return render_template("hello.html",
            # contact=[{"name":"  ", "  ": "  "},
                        #{"name": "  ", "  ": "  "}]
         #jinja- {% for contact in contacts %}
                    #<p>{{ contact.name}} live in {{contact.house}}</p>
                #{% endfor %}
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
        # user input name is symbol. render apology if input blank or does not exist per lookup
        # user input shares as text field whose name is shares. render apology if input is not positive int
        # submit user input via post or buy
        # redirect user to homepage upon purchase
    # lookup stock price, SELECT cash user has in users
    # add new tables to finance.db to track purchaase.
        # decide table names and fields UNIQUE or non-UNIQUE
        # CREATE TABLE to add new tables
        # run SQL statement on DB to purchase stock. is enough cash. if not return apology
        # update cash to reflect purchase

    # When for submit via POST, purchase the stock so long as user can afford it

    return apology("TODO")


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
        # text field name is symbol
        # creat template quote.html

    # When submitted via POST, use lookup function for  stock symbol and display results
        # lookup takes stock symbol and returns stock quote
        # if lookup successful, function returns dictionary with name,price,symbol
            # create template quoted.html
            # display name, price,symbol with html
            # python- return render_template("hello.html", name="Brian"
            # Jinja template- <p. hello, {{ name }}</p>
        # if lookup unsucceful, function returns none
    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # when requested via GET, display registration form
     # create a new template for registraion from templates folder
        # borrow from login.html
   if request.method == "GET":
    return render_template("register.html")

else
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

        # create a new template for registraion from templates folder
        # borrow from login.html
        # HTML <input name= "password".../>
        # python request.form.get("password")
        # prompt user for username, password,and confirmation
            # confirm (if field is blank return apology)
            # if password and confirmation dont match return an apology
            # if username is taken return apology
            # database should use generate_password_hash to generate password
    # when form is submitted via POST, check for possible errors and insert the new user in users table
        # use db.execute
        # use ? as placeholder
    #log user in
        # session["user_id"] keeps track of which user is logged in
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
