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

# @app.route("/fatsecret")
# def get_food_information():
#     """"search for food details on FatSecret"""

#     url = f"https://platform.fatsecret.com/js?key=23a92470c57a4a4ba460c8f0030927e9&auto_load=true"
#     payload = {'apikey': API_KEY}

#     response = requests.get(url, params=payload)

#     food = response.json()
    
#     return render_template('fatsecret.html')

@app.route('/calculator')
def calculator_page():
    """calculate user calories and macros page"""
    return render_template('calculator.html')

@app.route('/index')
def index_page():
    """" index page with all diaries """
    return render_template('index.html')

@app.route('/food', methods=['POST' , 'GET'])
def foods():
    """enter food items in food diary """
    food_name = request.form.get('food_name')
    calories = request.form.get('calories')
    protein = request.form.get('protein')
    carb = request.form.get('carb')
    fat = request.form.get('fat')

    user_id = session['user_id']

    food = crud.create_food(food_name, calories, protein, carb, fat, user_id)
    foods = crud.get_food(food_name)
    # logged_food= crud.get_food(user_id)

    return render_template('food.html' , foods=foods)

# @app.route('/all_food')
# def all_foods():
#     """ view all food items """
#     foods = crud.get_food()
#     return render_template('all_food.html', foods=foods)


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
        flash(f"Successfully logged in!")
    
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

@app.route('/questions', methods=['POST' , 'GET'])
def meals_macros_questionare():
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
    questionare_info = crud.questionare(gender, age, height, weight, activity, user_id)

    if user:
        flash("already have an account")
    else: 
        crud.questionare(age, gender, height, weight, activity)

    return render_template('profile.html')

@app.route('/goals', methods=['POST' , 'GET'])
def fitness_goals():
    # fitness_goal = request.form.get('goals')
    strength = request.form.get('strength')
    running = request.form.get('running')
    weight_loss = request.form.get('weight_loss')
    consistency = request.form.get('consistency')
    stretching = request.form.get('stretching')
    high_intensity_training = request.form.get('high_intensity_training')
    nutrition = request.form.get('nutrition')
    overall_health = request.form.get('overall_health')

    user_id=session['user_id']
    goal = crud.create_goal(user_id, strength, running, weight_loss, consistency, stretching, high_intensity_training, nutrition, overall_health)
    
    return render_template('goals.html')

# @app.route('/calculations' , methods=['POST' , 'GET'])
# def calculate_cal_macros():
#     """ calculate user cals and macros """
#     for gender in meals_macros_questionare():
#         if gender == "male":
#             bmr = (4.536 * weight) + (15.88 * height) - (5 * age) + 5
#             return bmr
#         if gender == "female":
#             bmr = (4.536 * weight) + (15.88 * height) - (5 * age) - 161
#             return bmr 

#         for activity in meals_macros_questionare():
#             if activity == "low":
#                 activity_level = 1.2
#                 return activity_level 
#             if activity == "moderate":
#                 activity_level = 1.5
#                 return activity_level 
#             if activity == "high":
#                 activity_level = 1.9
#                 return activity_level 

#                 tdee = (float(bmr) * float(activity))
#                 deficit = (float(tdee) - 500)
#                 macros = ((protein_goal == (round(deficit * 0.40))), (carb_goal == (round(deficit * 0.40))), (fat_goal == (round(deficit * 0.20))))
#                 macro_by_grams =  ((round(protein_goal / 4)), (round(carb_goal / 4)),(round(fat_goal / 9)))

#                 flash(f"Your daily caloric goal is: {deifict} and your daily macro goals are {macros_by_grams}")

#                 user_id=session['user_id']
#                 calculator_info = crud.new_calculator(tdee, deficit, macros, user_id, questions_id, protein_goal, fat_goal, carb_goal)

#             if user:
#                 flash("already have an account")
#             else:
#                 crud.new_calculator(tdee, deficit, macros, protein_goal, fat_goal, carb_goal)

#         return render_template('results.html')

    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)