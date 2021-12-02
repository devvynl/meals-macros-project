""" Model for meals & macros propject """
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ A user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(50))
    # weight = db.Column(db.Integer)
    # height = db.Column(db.Integer)
    # age = db.Column(db.Integer)
    # fitness_goal = db.Column(db.String)
    # goal_weight = db.Column(db.Integer)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class CaloriesMacros(db.Model):
    """ user's calories & macros """

    __tablename__ = "calories_macros"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    caloric_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    macro_id = db.Column(db.Integer, primary_key=True)
    daily_caloric_intake = db.Column(db.Integer)
    daily_protein_goal = db.Column(db.Integer)
    daily_carb_goal = db.Column(db.Integer)
    daily_fat_goal = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    user = db.relationship("User", backref="calories_macros")

    def __repr__(self):
        return f"<CaloriesMacros caloric_id={self.caloric_id} macro_id={self.macro_id}>"

class Diet(db.Model):
    """ user's diet preference """

    __tablename__ = "diet_preference"

    diet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    diet = db.Column(db.String)

    user = db.relationship("User", backref="diet_preference")

    def __repr__(self):
        return f"<Diet diet_id={self.diet_id} diet={self.diet}>"

class Goal(db.Model):
    """ user's fitness goals """

    __tablename__ = "goals"

    goal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fitness_goal = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="goals")

    def __repr__(self):
        return f"<Goal goal_id={self.goal_id} fitness_goal={self.fitness_goal}>"

# class User_meals(db.Model):
#     """ user's meals created by the user """

#     __tablename__ = "meals"

#     meal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
#     meal_name = db.Column(db.String)
#     meal_calories = db.Column(db.Integer)
#     meal_fat = db.Column(db.Integer)
#     meal_carb = db.Column(db.Integer)
#     meal_protein = db.Column(db.Integer)

#     user = db.relationship("User", backref="meals")

#     def __repr__(self):
#         return f"<User_meals meal_id={self.meal_id} meal_name={self.meal_name} meal_calories={self.meal_calories}>"

class Food(db.Model):

    __tablename__ = "foods"

    food_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_name = db.Column(db.String)
    total_calories = db.Column(db.Integer)
    total_fat = db.Column(db.Integer)
    total_carbs = db.Column(db.Integer)
    total_protein = db.Column(db.Integer)

    def __repr__(self):
        return f"<Food food_id{self.food_id} food_name{self.food_name}>"

# class User_tracking(db.Model):

#     __tablename__ = "tracking"

#     tracking_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
#     food_id = db.Column(db.Integer, db.ForeignKey("foods.food_id"))
#     deduct_daily_calories = db.Column(db.Integer)
#     deduct_daily_macros = db.Column(db.Integer)
#     date = db.Column(db.DateTime)

#     user = db.relationship("User", backref="tracking")
#     food = db.relationship("Food", backref="tracking")

#     def __repr__(self):
#         return f"<User_tracking tracking_id{self.tracking_id} deduct_daily_calories{self.deduct_daily_calories} deduct_daily_macros{self.deduct_daily_macros}>"

class UserQuestions(db.Model):

    __tablename__ = 'questions'

    questions_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    activity = db.Column(db.String)

    user = db.relationship("User", backref="questions")

    def __repr__(self):
        return f"<UserQuestions questions_id{self.questions_id} user_id={self.user_id}>"

class UserCalculations(db.Model):

    __tablename__ = 'calculations'

    calculations_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tdee = db.Column(db.Integer)
    deficit = db.Column(db.Integer)
    macros = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    questions_id = db.Column(db.Integer, db.ForeignKey("questions.questions_id"))
    protein_goal = db.Column(db.Integer)
    fat_goal = db.Column(db.Integer)
    carb_goal = db.Column(db.Integer)

    user = db.relationship('User', backref="calculations")
    userquestions = db.relationship('UserQuestions' , backref='calculations')

    def __repr__(self):
        return f"<UserCalculations calculations_id{self.calculations_id} user_id={self.user_id} questions_id={self.questions_id}>"

def connect_to_db(flask_app, db_uri="postgresql:///calories", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("! ! ! Connected to the db ! ! !")

if __name__ == "__main__":
    from server import app 

    connect_to_db(app)