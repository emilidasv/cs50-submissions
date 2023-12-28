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

    # Query database for username
    print(" ")
    print("INDEX ")
    print(" ")

    user_portfolio = db.execute(
       "SELECT symbol, SUM(shares) as total_shares FROM trades WHERE userid = :userid GROUP BY symbol HAVING total_shares > 0", userid=session["user_id"])
    user_cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])[0]["cash"]
    print(" ")
    print("INDE3 ")
    print(" ")
    print (user_cash)
    #update user_portfolio with stock current price and total actual price of shares
    total_value = user_cash
    grand_total = user_cash
    print("INDE5 ")

    for stock in user_portfolio:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["value"] = stock["price"] * stock["total_shares"]
        total_value += stock["value"]
        grand_total += stock["value"]
        print("index6")
    #print(user_portfolio[0])
    return render_template("index.html", user_portfolio=user_portfolio, user_cash=user_cash, total_value=total_value, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_nbr = request.form.get("shares")

        # Ensure symbol is not blank
        if symbol == "":
            return apology("MISSING SYMBOL", 400)
        if shares_nbr == "" or shares_nbr.isalpha():
            return apology("MISSING SHARES", 400)
        if (not shares_nbr.isdigit()):
            return apology("fractional not supported", 400)
        if int(shares_nbr) <= 0:
            return apology("share number can't be negative number or zero!", 400)

        stock_quote = lookup(symbol)

        if not stock_quote:
            return apology("INVALID SYMBOL", 400)

        total_cost = int(shares_nbr) * stock_quote["price"]
        print(' ')
        print('BUY')
        print(' ')
        print("user_id")
        print("id")

        user_cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id= session["user_id"])[0]["cash"]

        print('total_cost')
        print(total_cost)
        print('user_cash')
        print(user_cash)
        if user_cash < total_cost:
            return apology("CAN'T AFFORD", 400)

        else:
            print('everything Ok so far')
            #print('cash')
            #print(user_cash)
            #userid= session["user_id"]
            #print(userid)
            db.execute("INSERT INTO trades (userid, symbol, shares, price) VALUES(?, ?, ?, ?)",
                      session["user_id"], stock_quote['symbol'], int(shares_nbr), stock_quote['price'])
        #cash = user_cash[0]["cash"]
            #print('cash')
            #print(user_cash)
            userid= session["user_id"]
            #print(userid)
            #print(" ")
            print(" ")
            print(" ")
            print(symbol)
            print(shares_nbr)
            print(total_cost)

            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash - total_cost, session["user_id"])
            #db.execute("INSERT INTO trades( userid, symbol, shares, price) VALUES (:userid, :symbol, :shares, :price  )",
        #               id=session["user_id"], symbol=symbol, shares=shares, price=price)

            flash(f"Bought! Symbol: {symbol} Shares:{shares_nbr} Price: {usd(total_cost)} ")
            return redirect("/")

    # User reached route via GET
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Query database for username & transactions
    user_transactions = db.execute(
        "SELECT id, symbol, shares, price FROM trades WHERE userid = ? ORDER BY id", session["user_id"])

    return render_template("history.html", user_transactions=user_transactions)

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Show username """
    rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    name=rows[0]['username']
    print('name')
    print(name)
    oldhashcode =rows[0]['hash']
    print('oldhashcode')
    print(oldhashcode)

    if request.method == "POST":
           #print('passw')
           #newname = request.form.get("newname")

        # Ensure username was submitted
        if not request.form.get("newname"):
            return apology("must provide a new username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for the new username
        newrows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("newname"))

        #make sure that this new username doesn;t exist in database
        if len(newrows) != 0:
            return apology("invalid username ", 403)

        #make sure that the user gives correct passwrod
        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid  password", 403)


        #update new name in database
        db.execute("UPDATE users SET username = ? WHERE id = ?", request.form.get("newname"), session["user_id"])


        return render_template("account.html", user_name=request.form.get("newname"))


    else:
        return render_template("account.html", user_name=name)

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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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

     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        # Ensure symbol is not blank
        if symbol == "":
            return apology("input is blank", 400)

        stock_quote = lookup(symbol)
        if not stock_quote:
            return apology("INVALID SYMBOL", 400)
 ##       else:
 ##       return render_template("quote.html", symbol=stock_quote)
        return render_template("quote.html", stock_quote=stock_quote)

 #   # User reached route via GET
    else:
       return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
   # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Validate submission
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure password == confirmation
        if not (password == confirmation):
            return apology("the passwords do not match", 400)

        # Ensure password not blank
        if password == "" or confirmation == "" or username == "":
            return apology("input is blank", 400)

        # Ensure username does not exists already
        if len(rows) == 1:
            return apology("username already exist", 400)
        else:
            hashcode = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashcode)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        print(" ")
        print("SELL")
        print(" ")
        symbol = request.form.get("symbol")
        shares_nbr = request.form.get("shares")

        # Ensure symbol is not blank
        #if symbol == "":
        #    return apology("MISSING SYMBOL", 400)
        #if shares_nbr == "" or shares_nbr.isalpha():
        #    return apology("MISSING SHARES", 400)
        #if not is_int(shares_nbr):
        #    return apology("fractional not supported", 400)
        #if int(shares_nbr) <= 0:
        #    return apology("share number can't be negative number or zero!", 400)
        stock_quote = lookup(symbol)


        if not stock_quote:
            return apology("INVALID SYMBOL", 400)

        user_portfolio = db.execute(
            "SELECT id, symbol, SUM(shares) FROM trades WHERE userid = ? AND symbol = ? GROUP BY symbol HAVING SUM(shares)>0 ", session["user_id"], stock_quote['symbol'])
        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if user_portfolio[0]["SUM(shares)"] < int(shares_nbr):
            return apology("TOO MANY SHARES", 400)
        else:
            # update user_portfolio with based on sell transaction info

            currentprice = stock_quote['price'] * int(shares_nbr)
            cash = user_cash[0]["cash"]
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + currentprice, session["user_id"])
            db.execute("INSERT INTO trades (userid, symbol, shares, price) VALUES(?, ?, ?, ?)",
                       session["user_id"], stock_quote['symbol'], -int(shares_nbr), stock_quote['price'])
            flash('Sold!')
        return redirect("/")

    # User reached route via GET
    else:
        user_portfolio = db.execute(
            "SELECT id, symbol, SUM(shares) FROM trades WHERE userid = ? GROUP BY symbol HAVING SUM(shares)>0 ORDER BY symbol", session["user_id"])

        return render_template("sell.html", user_portfolio=user_portfolio)
