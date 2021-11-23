##classes for Orders table related tasks
from operator import truediv
import os
from dotenv import load_dotenv
from decouple import config
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
from models import Orders,db
from flask import Flask, jsonify,Blueprint
from sqlalchemy import exc

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

class Order_Builder:
    def make_Order(Client,Employee,Product,Brand,Accessory,Amount,Status,Service,Comments,Add_date):
        ## Makes the Order
        try:
            query = Orders(Client=Client,Employee=Employee,Product=Product,Brand=Brand,Accessory=Accessory,Price=Amount,Status=Status,Service=Service,Comments=Comments,Add_date=Add_date,Up_date=Add_date)
            db.session.add(query)
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}
    def update_Order(Order_no,Client,Employee,Product,Brand,Accessory,Amount,Status,Service,Comments,Up_date):
        ## Updates Order Values
        try:
            Current_Order = Orders.query.filter_by(Order_no=Order_no).first()
            if(Current_Order==None):
                return {"Status":False}
            Current_Order.Client = Client
            Current_Order.Employee = Employee
            Current_Order.Product = Product
            Current_Order.Brand = Brand
            Current_Order.Accessory = Accessory
            Current_Order.Amount = Amount
            Current_Order.Status = Status
            Current_Order.Service = Service
            Current_Order.Comments = Comments
            Current_Order.Up_date = Up_date
            #modify the row
            db.session.commit()
            return {"Status":True}
        except exc.SQLAlchemyError:
            return {"Status":False}

    def grab_Orders():
        ## Grab Orders data from db
        all_data = Orders.query.all()
        final_data = []
        for i in range(len(all_data)):
            row = {"Order_no":all_data[i].Order_no,"Deleted":all_data[i].Deleted,"Client":all_data[i].Client,
            "Employee":all_data[i].Employee,"Product":all_data[i].Product,"Brand":all_data[i].Brand,"Accessory":all_data[i].Accessory,
            "Price":float(all_data[i].Price),"Status":all_data[i].Status,"Service":all_data[i].Service,"Comments":all_data[i].Comments,
            "Add_date":all_data[i].Add_date,"Up_data":all_data[i].Up_date
            }
            final_data.append(row)
        return final_data[::-1]

    def del_Orders(Order_no):
        ## Delete client from the database
        ## Does not actually delete from database
        ## Has a checker to see that flags it to be hidden
        ## Frontend deals with the rest
        try:
            current_Orders = Orders.query.filter_by(Order_no=Order_no).first()
            current_Orders.Deleted = True
            db.session.commit()
            #delete user from db
            return {"Status": True}
        except exc.SQLAlchemyError:
            return {"Status":False}


'''
    Order_no = db.Column(db.Integer , primary_key=True, unique=True)
    Deleted = db.Column(db.Boolean, default=False, nullable=False)
    Client = db.Column(db.String(255), unique=True, nullable=False)
    Employee = db.Column(db.String(255), unique=True, nullable=False)
    Product = db.Column(db.String(255), unique=True, nullable=False)
    Brand = db.Column(db.String(255), unique=True, nullable=False)
    Accessory = db.Column(db.String(255), unique=True, nullable=False)
    Price = db.Column(db.Numeric, nullable=False)
    Status = db.Column(db.String(255), nullable=False)
    Service = db.Column(db.String(500), nullable=False)
    Comments = db.Column(db.String(500), nullable=False)
    Add_date = db.Column(db.String(255), nullable=False)
    Up_date = db.Column(db.String(255), nullable=False)

'''