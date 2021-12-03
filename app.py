from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///inventory.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/room_1", methods=["GET", "POST"])
def room_1():
    if request.method == "POST":
        return render_template("room_2.html")
    else:
        return render_template("room_1.html")

@app.route("/room_2", methods=["GET", "POST"])
def room_2():
    if request.method == "POST":
        return render_template("room_3.html")

@app.route("/room_3", methods=["GET", "POST"])
def room_3():
    if request.method == "POST":
        return render_template("end.html")

@app.route("/end", methods=["GET", "POST"])
def end():
    if request.method == "POST":
        return render_template("homepage.html")

