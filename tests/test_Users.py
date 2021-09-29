## Will be used to test the User related endpoints 
import json


def test_Insert(app, client): 
    ##Tests to see if data inserts into db
    del app
    res = client.get('Users/mk_user/John Doe/Doe123')
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))


def test_Validate(app, client): 
    ##Tests to see is validated
    del app
    res = client.get('Users/validate_user/John Doe/Doe123')
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))

def test_Update(app, client): 
    ##Tests to see if row will update into db 
    del app
    res = client.get('Users/update_user/John Doe/Doe1234') ##New password
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))

def test_Delete(app, client): 
    ##Tests to see if row will delete from db
    del app
    res = client.get('Users/delete_user/John Doe/Doe1234') 
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


