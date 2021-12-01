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

for n in range(3):
    email = f"user{n}@test.com"  
    password = "test"
    name= f"testusername{n}"
    lname=f"testlastname{n}"
    user = crud.create_user(email, password, name, lname)


