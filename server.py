""" server for meals & macros project """
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
# from fatsecret import Fatsecret
import crud
import os
# import requests


from jinja2 import StrictUndefined

# FOOD_QUOTES = [
#     "Be Better - Kobe",
#     "You may not be there yet, but you're closer than you were yesterday!", 
#     "It's a beautiful day to be alive!", 
#     "Eating well is a form of self respect", 
#     "Hard work pays off!"
# ]

app = Flask(__name__)
app.secret_key = "dev"
# fs = Fatsecret(consumer_key, consumer_secret)
app.jinja_env.undefined = StrictUndefined

# API_KEY = os.environ['MYFITNESSPAL_KEY']

# @app.route('/food-quotes')
# def quotes():
#     """famous fitness quotes for food diary page"""
#     return random.choice(FOOD_QUOTES)

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
    all_food=crud.get_all_food(user_id)

    if user not in session:
        redirect('/login-page')
       
    return render_template('food.html', foods=user_foods, all_food=all_food)

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
    
    # return redirect('/')
    return render_template('homepage.html' , user=user)


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
        
    
    return render_template('deficit-macros.html' , user=user)

@app.route('/logout')
def confirm_logout():
    """confirm user logged out """
    if 'user' in session: 
        session.pop('user', None)
        flash('Logged out.')
    else: 
        flash('Logged in.')
    
    return render_template('homepage.html')


def calculate_cal_macros(gender, age, height, weight, activity):
    """ calculate user cals and macros """
    age = int(age)
    height = int(height)
    weight = int(weight)
    
    # for gender in meals_macros_questionare():
    if gender == "male":
        bmr = (4.536 * weight) + (15.88 * height) - (5 * age) + 5
            
    elif gender == "female":
        bmr = (4.536 * weight) + (15.88 * height) - (5 * age) - 161
            
     
    if activity == "low":
        activity_level = 1.2
                
    elif activity == "moderate":
        activity_level = 1.5
            
    elif activity == "high":
        activity_level = 1.9
            
    tdee = (float(bmr) * float(activity_level))
    deficit = round(float(tdee) - 500)
    protein_goal = round(deficit * 0.40)
    carb_goal = round(deficit * 0.40)
    fat_goal = round(deficit * 0.20)
    protein_macros = round(protein_goal / 4)
    carb_macros = round(carb_goal / 4)
    fat_macros = round(fat_goal / 9)
    
    return (deficit, 'protein:',protein_macros, 'carb:',carb_macros, 'fat:',fat_macros)

@app.route('/questions', methods=['POST'])
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
    user_id = session.get('user_id')
    
    # print(gender, age, height, weight, activity, user_id)
    questionare_info = crud.questionare(gender, age, height, weight, activity, user_id)
    result = calculate_cal_macros(gender, age, height, weight, activity)
    # print(f"Your daily caloric goal is: {result[0]} and your daily macro goals are {result[1]}, {result[2]}, {result[3]}")


    if not user_id:
        return redirect('/login')
    else: 
        crud.questionare(gender, age, height, weight, activity, user_id)
    return render_template('index.html', deficit=result[0], macros_by_grams=result[1:])
    

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

    return redirect('/index')

@app.route('/goals', methods=['GET'])
def get_user_goals():
    """enter food items in food diary """

    user_id = session['user_id']
    user_goals = crud.get_goals(user_id)

    if user not in session:
        redirect('/login-page')
       
    return render_template('goals.html', user_goals=user_goals)
    
@app.route('/exercise', methods=['POST' , 'GET'])
def track_exercise():
    """ track exercise """
    exercise = request.form.get('exercise')

    user_id =session['user_id']

    return render_template('exercise.html', exercise=exercise)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)