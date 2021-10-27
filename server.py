""" server for meals & macros project """

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import requests

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ['MYFITNESSPAL_KEY']

@app.route('/')
def homepage():
    """show homepage"""
    return render_template('homepage.html')

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

@app.route('/user' , methods=['POST'])
def users():
    """create new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Already a user!')
    else: 
        crud.create_user(email,password)
        flash('User created!')
    
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    """user login"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash('email or password incorrect')
    else:
        session['user_email'] = user.email 
        flash(f"Welcome, {user.email}!")
    
    return redirect('/')

@app.route('/meal' , methods=['POST'])
def meal():
    """user created meal"""

    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0.", debug=True)