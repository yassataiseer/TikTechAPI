##classes for Services table related tasks
from operator import truediv
import os
from dotenv import load_dotenv
from decouple import config
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
from models import Services,db
from flask import Flask, jsonify,Blueprint
from sqlalchemy import exc

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

services_template = Blueprint("services_template",__name__)## extends app.py


class Service:
    def add_service(Service_name,Service_purpose,Service_cost):
        ## Add a new service to database
        try:
            query = Services(Service_Name=Service_name,Service_Purpose=Service_purpose,Service_Cost=Service_cost)
            db.session.add(query)
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def delete_service(Service_name):
        ## Deletes service from database 
        try:
            Services.query.filter_by(Service_Name=Service_name).delete()
            db.session.commit()
            return {"Status": True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def update_service(Service_name,Service_purpose,Service_cost):
        ## Updates existing service row
        try:
            current_service = Services.query.filter_by(Service_Name=Service_name).first()
            current_service.Service_Name = Service_name
            current_service.Service_Purpose = Service_purpose
            current_service.Service_Cost = Service_cost
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}

    def grab_services():
        ## Grab all data from services
        all_data = Services.query.all()
        final_data = []
        for i in range(len(all_data)):
            row = {"Service_name":all_data[i].Service_Name,"Service_purpose":all_data[i].Service_Purpose,
            "Service_cost":float(all_data[i].Service_Cost)}
            final_data.append(row)
        return final_data
