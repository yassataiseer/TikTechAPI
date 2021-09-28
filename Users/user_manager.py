
##views for Users table related tasks
import mysql.connector
import os
from dotenv import load_dotenv
from decouple import config
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
from models import Users,db
from flask import Flask, jsonify,Blueprint

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

user_template = Blueprint("user_template",__name__)## extends app.py
class Alluser:
    def all_users(self):
        #grabs all users from Users Table
        all_data = Users.query.all()
        print(all_data[0].Username)
        data = ["Username","Password"]
        final_data = []
        for i in range(len(all_data)):
            print(all_data[i].Username)
            row = {"Username":all_data[i].Username,"Password":all_data[i].Password}
            final_data.append(row)
        return final_data
class user:
    def __init__(self,username,password):
        self.username =  username
        self.password = password
        #convert to sha256 for user's privacy

    def connect():
        ##debugging function
        db =mysql.connector.connect(
        host = config('HOST') ,
        user = config('USERNAME') ,
        passwd = config('PASSWORD'),
        database = config('DATABASE'))
        return db 
    def add_user(self):
        if not user.check_if_user_exists(self):
            query = Users(Username=self.username,Password=self.password)
            db.session.add(query)
            db.session.commit()
            #add user to db
            return {"Status" : True}
        return {"Status" : False}

    def delete_user(self):
        Users.query.filter_by(Username=self.username).delete()
        db.session.commit()
        #delete user from db
        return {"Status": True}

    def check_user(self):
        exists = bool(db.session.query(Users).filter_by(Username=self.username,Password=self.password).first())
        #check to see if user exists inside of database
        #meant to validate user
        return {"Status" : exists}
        
    def check_if_user_exists(self):
        exists = bool(db.session.query(Users).filter_by(Username=self.username).first())
        #check to see if the Username is already taken.
        return exists
    
    def update_users(self):
        change_psswd = Users.query.filter_by(Username=self.username).first()
        #Find row where username is equal to Yassa Taiseer
        if(change_psswd==None):##if it does not exist
            return {"Status":False}

        change_psswd.Password = self.password
        #modify the password
        db.session.commit()
        return {"Status":True}


#add = user("Yassa Taiseer","yassa123")
#print(add.add_user())
#print(boolean.delete_user())





