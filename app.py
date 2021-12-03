from cs50 import SQL
from flask import Flask, redirect, render_template, request
from functools import wraps

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///inventory.db")

solved = {1: False, 2: False, 3: False, 4: False}

def solve_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # figure out how to check if previous room is solved
        if False:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("homepage.html")

@app.route("/room_1", methods=["GET", "POST"])
@solve_required
def room_1():
    if request.method == "POST":
        return redirect("/room_2")
    return render_template("room_1.html")

@app.route("/room_2", methods=["GET", "POST"])
@solve_required
def room_2():
    if request.method == "POST":
        return redirect("/room_3")
    else:
        return render_template("room_2.html")

@app.route("/room_3", methods=["GET", "POST"])
@solve_required
def room_3():
    if request.method == "POST":
        return redirect("/end")
    else:
        return render_template("room_3.html")

@app.route("/end", methods=["GET", "POST"])
@solve_required
def end():
    if request.method == "POST":
        return redirect("/homepage")
    return render_template("end.html")