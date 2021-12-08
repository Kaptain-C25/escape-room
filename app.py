import re
from flask import Flask, redirect, render_template, request
from functools import wraps

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

solved = {0: True, 1: False, 2: False, 3: False, 4: False}
items = []

# decorator function to prevent room skipping through url
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
    global items
    items = []
    return render_template("homepage.html")

@app.route("/room_1", methods=["GET", "POST"])
@solve_required(1)
def room_1():
    global solved
    global items
    if request.method == "POST":
        if re.search('wasp', str(request.form.get("password")), re.IGNORECASE):
            solved[1] = True
            items = []
            return redirect("/room_2", code=303)
        else:
            return render_template("room_1.html", items=items)
    else:
        return render_template("room_1.html", items=items)

@app.route("/answer_1", methods=["POST"])
@solve_required(1)
def answer_1():
    global items
    form_1_1 = request.form.get("answer_1_1")
    if  form_1_1 != None and form_1_1.lower() == 'w':
        if 'W' not in items:
            items += 'W'
    form_1_2 = request.form.get("answer_1_2")
    if  form_1_2 != None and form_1_2.lower() == 'a':
        if 'A' not in items:
            items += 'A'
    form_1_3 = request.form.get("answer_1_3")
    if  form_1_3 != None and form_1_3.lower() == 's':
        if 'S' not in items:
            items += 'S'
    form_1_4 = request.form.get("answer_1_4")
    if  form_1_4 != None and form_1_4.lower() == 'p':
        if 'P' not in items:
            items += 'P'
    return render_template("room_1.html", items=items)

@app.route("/room_2", methods=["GET", "POST"])
@solve_required(2)
def room_2():
    global solved
    global items
    if request.method == "POST":
        if str(request.form.get("password")) == "7468":
            solved[2] = True
            items = []
            return redirect("/room_3", code=303)
        else:
            return render_template("room_2.html", items=items)
    else:
        return render_template("room_2.html", items=items)

@app.route("/answer_2", methods=["POST"])
@solve_required(2)
def answer_2():
    global items
    if request.form.get("answer_2_1") == "7":
        if '7' not in items:
            items += '7'
    if request.form.get("answer_2_2") == "4":
        if '4' not in items:
            items += '4'
    if request.form.get("answer_2_3") == "6":
        if '6' not in items:
            items += '6'
    if request.form.get("answer_2_4") == "8":
        if '8' not in items:
            items += '8'
    return render_template("room_2.html", items=items)

@app.route("/room_3", methods=["GET", "POST"])
@solve_required(3)
def room_3():
    global solved
    global items
    if request.method == "POST":
        if re.search('game', str(request.form.get("password")), re.IGNORECASE):
            solved[3] = True
            items = []
            return redirect("/end", code=303)
        else:
            return render_template("room_3.html", items=items)
    else:
        return render_template("room_3.html", items=items)

@app.route("/answer_3", methods=["POST"])
@solve_required(3)
def answer_3():
    global items
    form_3_1 = request.form.get("answer_3_1")
    if  form_3_1 != None and form_3_1.lower() == 'g':
        if 'G' not in items:
            items += 'G'
    form_3_2 = request.form.get("answer_3_2")
    if  form_3_2 != None and form_3_2.lower() == 'a':
        if 'A' not in items:
            items += 'A'
    form_3_3 = request.form.get("answer_3_3")
    if  form_3_3 != None and form_3_3.lower() == 'm':
        if 'M' not in items:
            items += 'M'
    form_3_4 = request.form.get("answer_3_4")
    if  form_3_4 != None and form_3_4.lower() == 'e':
        if 'E' not in items:
            items += 'E'
    return render_template("room_3.html", items=items)

@app.route("/end")
@solve_required(4)
def end():
    global solved
    solved = {0: True, 1: False, 2: False, 3: False}
    return render_template("end.html")