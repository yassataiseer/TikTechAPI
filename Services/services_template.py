## Views for the Services

from flask import Flask, json, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Services.services_manager import Service
from flask_cors import CORS



services_template = Blueprint("services_template",__name__)## extends app.py

api = Api(services_template)
CORS(services_template, resources={r"/api/*": {"origins": "*"}})


class mk_Service(Resource):
    def get(self,Service_name,Service_purpose,Service_cost):
        status = Service.add_service(Service_name,Service_purpose,Service_cost)
        return jsonify(status)

class all_Services(Resource):
    def get(self):
        data = Service.grab_services()
        return jsonify(data)


api.add_resource(mk_Service,"/mk_Service/<string:Service_name>/<string:Service_purpose>/<float:Service_cost>")##creates client
api.add_resource(all_Services,"/all_Services")##creates client
