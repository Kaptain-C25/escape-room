from cs50 import SQL
from flask import Flask, redirect, render_template, request
from functools import wraps

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///inventory.db")

solved = {0: True, 1: False, 2: False, 3: False, 4: False}

def solve_required(loc):
    def test(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if solved[loc - 1] == False:
                return redirect(f"/room_{loc - 1}")
            return f(*args, **kwargs)
        return decorated_function
    return test

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def homepage():
    global solved
    solved = {0: True, 1: False, 2: False, 3: False, 4: False}
    return render_template("homepage.html")

@app.route("/room_1", methods=["GET", "POST"])
@solve_required(1)
def room_1():
    global solved
    if request.method == "POST":
        solved[1] = True
        return redirect("/room_2", code=303)
    else:
        return render_template("room_1.html")

@app.route("/room_2", methods=["GET", "POST"])
@solve_required(2)
def room_2():
    global solved
    if request.method == "POST":
        solved[2] = True
        return redirect("/room_3", code=303)
    else:
        return render_template("room_2.html")

@app.route("/room_3", methods=["GET", "POST"])
@solve_required(3)
def room_3():
    global solved
    if request.method == "POST":
        solved[3] = True
        return redirect("/end")
    else:
        return render_template("room_3.html")

@app.route("/end")
@solve_required(4)
def end():
    return render_template("end.html")