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
        return render_template("room_1.html")
    if request.method == "GET":
        return render_template("room_1.html")

