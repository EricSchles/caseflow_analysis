from flask import render_template, redirect,request,url_for,g,flash
from flask.ext.login import current_user, logout_user
from app import app
from app.models import *
from datetime import datetime
import json
import scipy as sp
from scipy import stats
import math
from app import flask_login,login_manager
import bcrypt
from tools import *

@login_manager.user_loader
def user_loader(email):
    users = Users.query.all()
    for user_obj in users:
        if email == user_obj.email:
            user = User()
            user.id = email
            return user
    return 

@login_manager.request_loader
def request_loader(request):
    users = Users.query.all()
    email = request.form.get("email")
    for user_obj in users:
        if email == user_obj.email:
            user = User()
            user.id = email
            user.is_authenticated = request.form.get("password") == user_obj.password
            return user
    return


def check_password(email,password):
    user_pw = str(Users.query.filter_by(email=email).first().password)
    print user_pw
    print password
    if bcrypt.hashpw(password,user_pw) == user_pw:
        return True
    else:
        return False
    
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    #explicitly force string type because of demands from bcrypt
    email = str(request.form.get("email"))
    password = str(request.form.get("password"))
    if check_password(email,password):
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for("splash_page"))
    return render_template("login.html",error="username or password was incorrect, please try again")
    
@app.route("/splash_page",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def splash_page():
    return render_template("splash_page.html",current_user=current_user)

@app.route("/sample_report",methods=["GET","POST"])
def sample_report():
    data, sorted_time_elapsed, time_elapsed, kurt, skew, var, mean = process_dates()
    return render_template(
        "sample_report.html",
        show_sorted=True,
        average=round(mean,3),
        standard_deviation=round(math.sqrt(var),3),
        skew=round(skew,3),
        kurtosis=round(kurt,3),
        time_elapsed=json.dumps(time_elapsed),
        sorted_time_elapsed=json.dumps(sorted_time_elapsed),
        data=data
    )

@app.route("/protected_report",methods=["GET","POST"])
@flask_login.login_required
def protected_report():
    return "Nothing to see here yet"

@app.route("/query_bar",methods=["GET","POST"])
def query_bar():
    if request.method=="POST":
        pass
    return "nothing"

@app.route("/logout")
@flask_login.login_required
def logout():
    logout_user()
    return redirect(url_for("splash_page"))
