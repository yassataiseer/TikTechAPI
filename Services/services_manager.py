##classes for Services table related tasks
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

services_template = Blueprint("services_template",__name__)## extends app.py


class Services:
    def add_service(Service_name,Service_purpose,Service_cost):
        ## Add a new service to database
        try:
            query = Services(Service_name=Service_name,Service_purpose=Service_purpose,Service_cost=Service_cost)
            db.session.add(query)
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def delete_service(Service_name):
        ## Deletes service from database 
        try:
            Services.query.filter_by(Service_name=Service_name).delete()
            db.session.commit()
            return {"Status": True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def update_service(Service_name,Service_purpose,Service_cost):
        ## Updates existing service row
        try:
            current_service = Services.query.filter_by(Service_name=Service_name).first()
            current_service.Service_name = Service_name
            current_service.Service_purpose = Service_purpose
            current_service.Service_cost = Service_cost
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}
            
    def grab_services():
        ## Grab all data from services
        all_data = Services.query.all()
        final_data = []
        for i in range(len(all_data)):
            row = {"Service_name":all_data[i].Service_name,"Service_purpose":all_data[i].Service_purpose,
            "Service_cost":all_data[i].Service_cost}
            final_data.append(row)
        return final_data
        

