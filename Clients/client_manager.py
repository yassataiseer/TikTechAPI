
##views for Users table related tasks
from operator import truediv
import mysql.connector
import os
from dotenv import load_dotenv
from decouple import config
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
from models import Clients,db
from flask import Flask, jsonify,Blueprint
from sqlalchemy import exc

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

user_template = Blueprint("user_template",__name__)## extends app.py

class Client:
    def add_Client(Name,Address,Postal_code,Email,Phone_number):
        try:
            query = Clients(Name=Name,Address=Address,PostalCode=Postal_code,Email=Email,Phone_No=Phone_number)
            db.session.add(query)
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def del_Client(id):
        try:
            current_client = Clients.query.filter_by(Id=id).first()
            print(current_client)
            current_client.Deleted = True
            db.session.commit()
            #delete user from db
            return {"Status": True}
        except exc.SQLAlchemyError:
            return {"Status":False}

