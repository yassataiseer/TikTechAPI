
##classes for Inventory table related tasks
from operator import truediv
import mysql.connector
import os
from dotenv import load_dotenv
from decouple import config
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
from models import Inventory,db
from flask import Flask, jsonify,Blueprint
from sqlalchemy import exc

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


class Inventory_Builder:
    def mk_Inventory(Item,Barcode,Price,Quantity,Status):
        ## Makes inventory
        try:
            query = Inventory(Item=Item,Barcode=Barcode,Price=Price,Quantity=Quantity,Status=Status)
            db.session.add(query)
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def update_Inventory(Item,Barcode,Price,Quantity,Status):
        ## Updates inventory values
        try:
            Current_Inventory = Inventory.query.filter_by(Item=Item).first()
            if(Current_Inventory==None):
                return {"Status":False}
            Current_Inventory.Item = Item
            Current_Inventory.Barcode = Barcode
            Current_Inventory.Price = Price
            Current_Inventory.Quantity = Quantity
            Current_Inventory.Status = Status
            #modify the row
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def grab_Inventory():
        ## Grab inventory data from db
        all_data = Inventory.query.all()
        final_data = []
        for i in range(len(all_data)):
            row = {"Item":all_data[i].Item,"Barcode":all_data[i].Barcode,
            "Price":float(all_data[i].Price),"Quantity":all_data[i].Quantity,"Status":all_data[i].Status}
            final_data.append(row)
        return final_data
    def delete_Inventory(Item):
        try:
            Inventory.query.filter_by(Item=Item).delete()
            db.session.commit()
            #delete user from db
            return {"Status": True}
        except exc.SQLAlchemyError:
            return {"Status":False}