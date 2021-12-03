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

@app.route('/calculator')
def calculator_page():
    """calculate user calories and macros page"""
    return render_template('calculator.html')

@app.route('/index')
def index_page():
    """" index page with all diaries """
    return render_template('index.html')

@app.route('/food', methods=['POST'])
def foods():
    """enter food items in food diary """
    food_name = request.form.get('food_name')
    calories = request.form.get('calories')
    protein = request.form.get('protein')
    carb = request.form.get('carb')
    fat = request.form.get('fat')

    user_id = session['user_id']

    food = crud.create_food(food_name, calories, protein, carb, fat, user_id)
    # foods = crud.get_food(food_name)
   
    return redirect('/food')
    

@app.route('/food', methods=['GET'])
def get_user_foods():
    """enter food items in food diary """

    user_id = session['user_id']
    user_foods = crud.get_all_food(user_id)

    if user not in session:
        redirect('/login-page')
       
    return render_template('food.html', foods=user_foods)

@app.route('/all_food')
def all_foods():
    user_id = session['user_id']
    all_food=crud.get_all_food(user_id)

    return render_template('all_food.html', all_food=all_food)
    
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
    
    return render_template('index.html' , user=user)

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
    # result = calculate_cal_macros(gender, age, height, weight, activity)
    # result = (f"Your daily caloric goal is: {deifict} and your daily macro goals are {macros_by_grams}")
    
    if user:
        redirect('/index')
    else: 
        crud.questionare(age, gender, height, weight, activity)

    return render_template('index.html')

@app.route('/goals', methods=['POST'])
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
    
    return redirect('/goals')

@app.route('/goals', methods=['GET'])
def get_user_goals():
    """enter food items in food diary """

    user_id = session['user_id']
    user_goals = crud.get_goals(user_id)

    if user not in session:
        redirect('/login-page')
       
    return render_template('goals.html', goals=user_goals)
    
# @app.route('/exercise', methods=['POST' , 'GET'])
# def track_exercise():
#     """ track exercise """
#     exercise = request.form.get('exercise')

#     user_id =session['user_id']

#     return render_template('exercise.html')

##### returning max recursion error- need to fix
# def calculate_cal_macros(gender, age, height, weight, activity):
#     """ calculate user cals and macros """
#     for gender in meals_macros_questionare():
#         if gender == "male":
#             bmr = (4.536 * weight) + (15.88 * height) - (5 * age) + 5
            
#         if gender == "female":
#             bmr = (4.536 * weight) + (15.88 * height) - (5 * age) - 161
            

#         for activity in meals_macros_questionare():
#             if activity == "low":
#                 activity_level = 1.2
                
#             if activity == "moderate":
#                 activity_level = 1.5
            
#             if activity == "high":
#                 activity_level = 1.9
            

#         tdee = (float(bmr) * float(activity))
#         deficit = (float(tdee) - 500)
#         macros = ((protein_goal == (round(deficit * 0.40))), (carb_goal == (round(deficit * 0.40))), (fat_goal == (round(deficit * 0.20))))
#         macro_by_grams =  (('PROTEIN:'),(round(protein_goal / 4)), ('CARB:'),(round(carb_goal / 4)), ('FAT:'),(round(fat_goal / 9)))

#         return deficit and macros_by_grams
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)