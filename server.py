""" server for meals & macros project """
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
# from fatsecret import Fatsecret
import crud
import os
# import requests


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
# fs = Fatsecret(consumer_key, consumer_secret)
app.jinja_env.undefined = StrictUndefined

# API_KEY = os.environ['MYFITNESSPAL_KEY']

@app.route('/')
def homepage():
    """show homepage"""
    return render_template('homepage.html')

@app.route('/login-page')
def login_page():
    """"show login page"""
    return render_template('login-page.html')

@app.route("/fatsecret")
def get_food_information():
    """"search for food details on FatSecret"""

    url = f"https://platform.fatsecret.com/js?key=23a92470c57a4a4ba460c8f0030927e9&auto_load=true"
    payload = {'apikey': API_KEY}

    response = requests.get(url, params=payload)

    food = response.json()
    
    return render_template('fatsecret.html')

@app.route('/calculator')
def calculator_page():
    """calculate user calories and macros page"""
    return render_template('calculator.html')

@app.route('/food')
def food():
    """view food options"""
    food = crud.create_food()
    return render_template('food.html', food=food)

@app.route('/tracking')
def tracking():
    """show users tracking"""
    tracking = crud.create_tracking()
    return render_template('tracking.html', tracking=tracking)

@app.route('/user', methods=['POST'])
def user():
    """create new user"""
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    lname = request.form.get('lname')

    user = crud.get_user_by_email(email)

    if user:
        flash('Already a user!')
    else: 
        crud.create_user(email, password, name, lname)
        flash('User created! Log into account.')
    
    return redirect('/')
    # return render_template('homepage.html' , user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    """process user login"""

    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    lname = request.form.get('lname')

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash('email or password incorrect')
    else:
        session['user_id'] = user.user_id
        session['name'] = user.name
        flash(f"Welcome, {user.name}!")
    
    return render_template('profile.html' , user=user)

@app.route('/logout')
def confirm_logout():
    """confirm user logged out """
    if 'user' in session: 
        session.pop('user', None)
        flash('Logged out.')
    else: 
        flash('Logged in.')
    
    return render_template('homepage.html')

@app.route('/questions', methods=['POST'])
def meals_macros_quiestionare():
    gender = request.form.get('gender')
    # print(gender)
    age = request.form.get('age')
    # print(age)
    height = request.form.get('height')
    # print(height)
    weight = request.form.get('weight')
    # print(weight)
    activity = request.form.get('activity')
    # return ("success")
    user_id=session['user_id']
    if user:
        flash("already have an account")
    else: 
        crud.questionare(age, gender, height, weight, activity)

    return render_template('fatsecret.html')

# @app.route('/meal' , methods=['POST'])
# def meal():
#     """user created meal"""
#     pass
    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)