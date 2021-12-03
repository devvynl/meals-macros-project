""" dropdb, createdb, use db.create_all to create tables, and  populate the db w/data """
 
import os 
import json 
from datetime import datetime 

import crud 
import model
import server 

os.system("dropdb calories --if-exists")
os.system("createdb calories")

model.connect_to_db(server.app)
model.db.create_all()

#load data from API/JSON file
with open("data/calories_macros.json") as f:
    project_data = json.loads(f.read())

#create food, store food in list so user can use them to add to food diary! 
# food_in_db = []
# for food in project_data:
#     food_name, calories, protein, carb, fat = (
#         food['food_name'],
#         food['calories'],
#         food['protein'],
#         food['carb'],
#         food['fat'],
#     )

#     db_food = crud.create_food(food_name, calories, protein, carb, fat)
#     food_in_db.append(db_food)


for n in range(3):
    email = f"user{n}@test.com"  
    password = "test"
    name= f"testusername{n}"
    lname=f"testlastname{n}"
    user = crud.create_user(email, password, name, lname)


