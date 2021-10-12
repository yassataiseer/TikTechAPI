## Views for the Inventory

from flask import Flask, json, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Inventory.inventory_manager import Inventory_Builder
from flask_cors import CORS



inventory_template = Blueprint("_template",__name__)## extends app.py

api = Api(inventory_template)
CORS(inventory_template, resources={r"/api/*": {"origins": "*"}})


class mk_Inventory(Resource):
    def get(self,Item,Barcode,Price,Quantity,Status):
        status = Inventory_Builder.mk_Inventory(Item,Barcode,Price,Quantity,Status)
        return jsonify(status)

class update_Inventory(Resource):
    def get(self,Item,Barcode,Price,Quantity,Status):
        status = Inventory_Builder.update_Inventory(Item,Barcode,Price,Quantity,Status)
        return jsonify(status)

class grab_Inventory(Resource):
    def get(self):
        status = Inventory_Builder.grab_Inventory()
        return jsonify(status)
class del_Inventory(Resource):
    def get(self,Item):
        status = Inventory_Builder.delete_Inventory(Item)
        return jsonify(status)

api.add_resource(mk_Inventory,"/mk_Inventory/<string:Item>/<string:Barcode>/<float:Price>/<string:Quantity>/<string:Status>")##creates Inventory
api.add_resource(update_Inventory,"/update_Inventory/<string:Item>/<string:Barcode>/<float:Price>/<string:Quantity>/<string:Status>")##Updates inventory
api.add_resource(grab_Inventory,"/grab_Inventory")##Updates inventory
api.add_resource(del_Inventory,"/del_Inventory/<string:Item>")



