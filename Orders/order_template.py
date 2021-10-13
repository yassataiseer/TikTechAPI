## Views for the Orders

from flask import Flask, json, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_cors import CORS
from Orders.order_manager import Order_Builder

order_template = Blueprint("order_template",__name__)## extends app.py

api = Api(order_template)
CORS(order_template, resources={r"/api/*": {"origins": "*"}})

class mk_Order(Resource):
    def get(self,Client,Employee,Product,Brand,Accessory,Amount,Status,Service,Comments,Add_date):
        status = Order_Builder.make_Order(Client,Employee,Product,Brand,Accessory,Amount,Status,Service,Comments,Add_date)
        return jsonify(status)

class update_Order(Resource):
    def get(self,Order_no,Client,Employee,Product,Brand,Accessory,Amount,Status,Service,Comments,Up_date):
        status = Order_Builder.update_Order(Order_no,Client,Employee,Product,Brand,Accessory,Amount,Status,Service,Comments,Up_date)
        return jsonify(status)

class all_Order(Resource):
    def get(self):
        status = Order_Builder.grab_Orders()
        return jsonify(status)

class del_Order(Resource):
    def get(self,Order_no):
        status = Order_Builder.del_Orders(Order_no)
        return jsonify(status)

api.add_resource(mk_Order,"/mk_Order/<string:Client>/<string:Employee>/<string:Product>/<string:Brand>/<string:Accessory>/<float:Amount>/<string:Status>/<string:Service>/<string:Comments>/<string:Add_date>")##creates order
api.add_resource(update_Order,"/update_Order/<int:Order_no>/<string:Client>/<string:Employee>/<string:Product>/<string:Brand>/<string:Accessory>/<float:Amount>/<string:Status>/<string:Service>/<string:Comments>/<string:Up_date>")##creates order
api.add_resource(all_Order,"/all_Order")
api.add_resource(del_Order,"/del_Order/<int:Order_no>")