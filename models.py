##Basic Database model for TikTechAPI
##Uses Flask-SQLAlchemy ORM
##MySQL based
##Written by Yassa Taiseer

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import  pymysql
#app = Flask(__name__)

db = SQLAlchemy()


class Users(db.Model):
    Username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    Password = db.Column(db.String(255),  nullable=False)

class Clients(db.Model):
    Name = db.Column(db.String(255), unique=True, nullable=False)
    Address = db.Column(db.String(300), unique=False, nullable=False)
    PostalCode = db.Column(db.String(50), unique=False, nullable=False)
    Email = db.Column(db.String(200), unique=False, nullable=False)
    Phone_No = db.Column(db.String(200), unique=False, nullable=False)
    Id = db.Column(db.Integer , primary_key=True, unique=True)
    Deleted = db.Column(db.Boolean, default=False, nullable=False)

class Services(db.Model):
    Service_Name = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
    Service_Purpose = db.Column(db.String(500), nullable=False)
    Service_Cost = db.Column(db.Numeric, nullable=False)

class Inventory(db.Model):
    Item = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
    Barcode  = db.Column(db.String(255),  nullable=False)
    Price = db.Column(db.Numeric, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.String(255), nullable=False)

class Orders(db.Model):
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
Order_no(Primary Key)
Deleted(boolean)
Client	(varchar)
Employee(varchar)[grab from Users]
Product (varchar)
Brand (varchar)
Accessory	(varchar)
$Amount (Decimal)
Status (varchar)	
Service (varchar)
Comments	(varchar)
Add Date (varchar)
Up Date (varchar)





Item(Varchar)(Primary Key)
Barcode Number(Varchar)
Price(Decimal)
Quantity(INT)
Status(Varchar)





Name(varchar)
Address
Postal code
Email
Phone Number
Id(Auto Increment)(primary key)
Deleted(boolean)


Service_Name(Varchar)(primary key)
Service Purpose(Varchar)
Service_Cost(Decimal)


class deliveries(db.Model):
    Username = db.Column(db.String(255), nullable=False, primary_key=True)
    Address = db.Column(db.String(255), unique=True, nullable=False)
    Latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    Item = db.Column(db.String(255), nullable=False)
    Price = db.Column(db.Float(), nullable=False)
    User_Info = db.Column(db.String(255), nullable=False)

'''