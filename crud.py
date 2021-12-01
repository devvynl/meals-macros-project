""" CRUD operations for meals and macros project """
from model import db, User, CaloriesMacros, Diet, Goal, Food, UserQuestions, connect_to_db
# from model import db, User, connect_to_db 

def create_user(email, password, name, lname):
    """ create a new  user """

    user = User(email=email, password=password, name=name, lname=lname)

    db.session.add(user)
    db.session.commit()

    return user 
    
def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_cals_macros(user, daily_caloric_intake, daily_protein_goal, daily_carb_goal, daily_fat_goal):

    """ create calorie and macros """

    calories_and_macros = Calories_macros(
        user=user,
        daily_caloric_intake=daily_caloric_intake, 
        daily_protein_goal=daily_protein_goal, 
        daily_carb_goal=daily_carb_goal, 
        daily_fat_goal=daily_fat_goal
    )

    db.session.add(calories_and_macros)
    db.session.commit()

    return calories_and_macros 

def create_diet(diet, user):

    """ create diet preference """

    diet = Diet(diet=diet, user=user)

    db.session.add(diet)
    db.session.commit()

    return diet 

def create_goal(user,fitness_goal):

    """ create user fitness goal """

    goal = Goal(fitness_goal=fitness_goal, user=user)

    db.session.add(goal)
    db.session.commit()

    return goal 

# def create_meal(user, meal_name, meal_calories, meal_protein, meal_carb, meal_fat):

#     """ create user meals """

#     meal = User_meals(
#         user=user, 
#         meal_name=meal_name, 
#         meal_calories=meal_calories, 
#         meal_protein=meal_protein, 
#         meal_carb=meal_carb,
#         meal_fat=meal_fat,
#     )

#     db.session.add(meal)
#     db.session.commit()

#     return meal 

def create_food(food_name, food_calories, total_fat, total_carb, total_protein):

    """ create food for user to use for tracking """ 

    food = Food( 
        food_name=food_name,
        food_calories=food_calories,
        total_fat=total_fat,
        total_carb=total_carb,
        total_protein=total_protein,
    )

    db.session.add(food)
    db.session.commit()

    return food

def create_tracking(user, food, deduct_daily_calroies, deduct_daily_macros):

    """ create tracking for user to enter food throughout the day """

    tracking = User_tracking(
        user=user,
        food=food,
        deduct_daily_calories=deduct_daily_calories,
        deduct_daily_macros=deduct_daily_macros,
    )

    db.session.add(tracking)
    db.session.commit()

    return tracking 

def questionare(gender, age, height, weight, activity):

    """ questionare information """

    questionare_info = User_questions(
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        activity=activity
    )

    db.session.add(questionare_info)
    db.session.commit()

    return questionare_info 


if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)
    