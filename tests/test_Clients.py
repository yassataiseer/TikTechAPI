## Will be used to test the Client related endpoints 
import json
import os
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
from models import Clients,db
from flask import Flask, jsonify,Blueprint
from sqlalchemy import exc

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


def test_InsertClient(app, client): 
    ##Tests to see if data inserts into db
    del app
    res = client.get('Clients/mk_Client/Jane Doe/123 Elm St/X5D 4J5/test@gmail.com/333888318893')
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))




'''
This tests the basic CRUD functions
of the User's blueprint endpoints.
This testing framework uses pytest
to run and setup use the following:

Setup: pip install pytest

Mac&Linux: python3 -m pytest

Windows 10: python -m pytest

'''

