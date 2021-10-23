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

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0.", debug=True)