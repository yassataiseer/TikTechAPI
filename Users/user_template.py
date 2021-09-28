from flask import Flask, json, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Users.user_manager import user
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS


user_template = Blueprint("user_template",__name__)## extends app.py

api = Api(user_template)
CORS(user_template, resources={r"/api/*": {"origins": "*"}})

auth = HTTPBasicAuth()##instance of basic auth




class mk_user(Resource):
    def get(self,Username,Password):
        new_user = user(Username,Password)
        status = new_user.add_user()
        return jsonify(status)

class validate_user(Resource):
    def get(self,Username,Password):
        validate_user = user(Username,Password)
        status = validate_user.check_user()
        return jsonify(status)

class update_user(Resource):
    def get(self,Username,Password):
        update_user = user(Username,Password)
        status = update_user.update_users()
        return jsonify(status)

class delete_user(Resource):
    def get(self,Username,Password):
        deleted_user = user(Username,Password)
        status = deleted_user.delete_user()
        return jsonify(status)

api.add_resource(mk_user,"/mk_user/<string:Username>/<string:Password>")##creates user
api.add_resource(validate_user,"/validate_user/<string:Username>/<string:Password>")##creates user
api.add_resource(update_user,"/update_user/<string:Username>/<string:Password>")##Update password
api.add_resource(delete_user,"/delete_user/<string:Username>/<string:Password>")##Update password




