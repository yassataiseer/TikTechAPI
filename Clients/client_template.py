## Views for the Clients

from flask import Flask, json, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Clients.client_manager import Client
from flask_cors import CORS


client_template = Blueprint("client_template",__name__)## extends app.py

api = Api(client_template)
CORS(client_template, resources={r"/api/*": {"origins": "*"}})



class mk_Client(Resource):
    def get(self,Name,Address,Postal_code,Email,Phone_number):
        status = Client.add_Client(Name,Address,Postal_code,Email,Phone_number)
        return jsonify(status)

class del_Client(Resource):
    def get(self,id):
        status = Client.del_Client(id)
        return jsonify(status)


api.add_resource(mk_Client,"/mk_Client/<string:Name>/<string:Address>/<string:Postal_code>/<string:Email>/<string:Phone_number>")##creates user
api.add_resource(del_Client,"/del_Client/<int:id>")##creates user

