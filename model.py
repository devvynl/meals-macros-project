""" Model for meals & macros propject """
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ A user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    age = db.Column(db.Integer)
    fitness_goal = db.Column(db.String)
    goal_weight = db.Column(db.Interger)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}"

class Calories_macros(db.Model):
    """ user's calories & macros """

    __tablename__ = "calories_macros"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    caloric_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    macro_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    daily_caloric_intake = db.Column(db.Integer)
    daily_protein_goal = db.Column(db.Integer)
    daily_carb_goal = db.Column(db.Integer)
    daily_fat_goal = db.Column(db.DateTime)

    user = db.relationship("User", backref="calories_macros")

    def __repr__(self):
        return f"<Calories_macros caloric_id={self.caloric_id} macro_id={self.macro_id}>"

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
    """ user's fitness goals """"

    __tablename__ = "goals"

    goal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fitness_goals = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="goals")

    def __repr__(self):
        return f"<Goal goal_id={self.goal_id} fitness_goal={self.fitness_goal}>"

class User_meals(db.Model):
    """ user's meals created by the user """

    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    meal_name = db.Column(db.String)
    meal_calories = db.Column(db.Integer)
    meal_fat = db.Column(db.Integer)
    meal_carb = db.Column(db.Integer)
    meal_protein = db.Column(db.Integer)

    user = db.relationship("User", backref="meals")

    def __repr__(self):
        return f"<User_meals meal_id={self.meal_id} meal_name={self.meal_name} meal_calories={self.meal_calories}>"

class 