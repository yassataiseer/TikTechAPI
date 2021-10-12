#main app file

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models import db
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from Users.user_template import user_template
from Clients.client_template import client_template
from Services.services_template import services_template
from Inventory.inventory_template import inventory_template
host = config('HOST') 
user = config('USERNAME') 
passwd = config('PASSWORD')
database = config('DATABASE')
#load env var
app = Flask(__name__)
api = Api(app)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(user_template,url_prefix="/Users")
app.register_blueprint(client_template,url_prefix="/Clients")
app.register_blueprint(services_template,url_prefix="/Services")
app.register_blueprint(inventory_template,url_prefix="/Inventory")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+passwd+'@'+host+'/'+database
##connect to mysql via SQLALCHEMY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_recycle': 299,
    'pool_timeout': 20,
    'pool_size': 10,
    'max_overflow': 5,
}
db.init_app(app)

with app.app_context():
    db.create_all()


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)