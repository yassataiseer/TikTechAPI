
##classes for Client table related tasks
from operator import truediv
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


class Client:
    def add_Client(Name,Address,Postal_code,Email,Phone_number):
        ## Add a new client to database
        try:
            query = Clients(Name=Name,Address=Address,PostalCode=Postal_code,Email=Email,Phone_No=Phone_number)
            db.session.add(query)
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}

    def del_Client(id):
        ## Delete client from the database
        ## Does not actually delete from database
        ## Has a checker to see that flags it to be hidden
        ## Frontend deals with the rest
        try:
            current_client = Clients.query.filter_by(Id=id).first()
            print(current_client)
            current_client.Deleted = True
            db.session.commit()
            #delete user from db
            return {"Status": True}
        except exc.SQLAlchemyError:
            return {"Status":False}

    def update_Client(Name,Address,Postal_code,Email,Phone_number,id):
        try:
            Current_client = Clients.query.filter_by(Id=id).first()
            #Find row where Id is = to the Clients row
            if(Current_client==None):##if it does not exist
                return {"Status":False}
            Current_client.Name = Name
            Current_client.Address = Address
            Current_client.Postal_code = Postal_code
            Current_client.Email = Email
            Current_client.Phone_number = Phone_number
            #modify the row
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}

    def all_Clients():
        #grabs all clients from Clients Table
        all_data = Clients.query.all()
        final_data = []
        for i in range(len(all_data)):
            row = {"Username":all_data[i].Name,"Address":all_data[i].Address,
            "Postal_code":all_data[i].PostalCode,"Email":all_data[i].Email,"Phone Number":all_data[i].Phone_No,"Deleted":all_data[i].Deleted,"Id":all_data[i].Id}
            final_data.append(row)
        return final_data
