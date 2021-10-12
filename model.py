""" Model for meals & macros propject """


class User(db.Model):
    """ A user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer , autoincrement=True, primary_key=True)
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

        user_id = db.Column(db.Integer , autoincrement=True, primary_key=True)
        caloric_id = db.Column
        macro_id = db.Column
        daily_caloric_intake = db.Column
        daily_protein_goal = db.Column
        daily_carb_goal = db.Column
        daily_fat_goal = db.Column
        date = db.Column
