# """calorie and macro calculator"""
# from model import db, UserQuestions, connect_to_db
# from crud import questionare 

# app = Flask(__name__)
# app.secret_key = "dev"

# @app.route('/questions' , ['POST' , 'GET'])
# def calculate_bmr(gender, weight, height, age):
#     # gender = "male" or "female"
#     for gender in get_user_info():
#         if gender == "male":
#             return (4.536 * weight) + (15.88 * height) - (5 * age) + 5
#         if gender == "female":
#             return (4.536 * weight) + (15.88 * height) - (5 * age) - 161

#     def user_activity(low, moderate, high):
#         if activity == "low":
#             activity_level = 1.2
#         elif activity == "moderate":
#             activity_level = 1.5
#         elif activity == "high":
#             activity_level = 1.9
#         return activity_level 

#     def calculate_tdee(tdee):
#         tdee = (float(bmr) * float(activity))
#         return tdee 

#     def calculate_cal_deficit(deficit):
#         deficit = (float(tdee) - 500)
#         return deficit 

#     def calculate_macros(macros):
#         macros = ((protein_goal == (round(deficit * 0.40))), 
#         (carb_goal == (round(deficit * 0.40))), 
#         (fat_goal == (round(deficit * 0.20))))
        
#         macro_by_grams =  ((round(protein_goal / 4)), 
#         (round(carb_goal / 4)),
#         (round(fat_goal / 9)))
#         return macro_by_grams


# def give_user_information(calories, macros):
#     print(f"Your daily caloric goal is: {deifict} and your daily macro goals are {macros_by_grams}")
#     render_template('index.html')
    
