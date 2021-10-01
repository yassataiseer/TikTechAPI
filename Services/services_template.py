## Views for the Services

from flask import Flask, json, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Services.services_manager import *
from flask_cors import CORS


services_template = Blueprint("services_template",__name__)## extends app.py

api = Api(services_template)
CORS(services_template, resources={r"/api/*": {"origins": "*"}})