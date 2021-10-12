## Will be used to test the Inventory related endpoints 
import json


def test_Insert_Inventory(app, client): 
    ##Tests to see if data inserts into Inventory table of the db
    del app
    res = client.get('/Inventory/mk_Inventory/iPhone Screen/9019980131/15.0/14/in stock')
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))


def test_Update_Inventory(app, client): 
    ##Tests to see if row will update into Inventory table of thedb 
    del app
    res = client.get('/Inventory/update_Inventory/iPhone Screen/9019980131/16.0/14/in stock') ##New price
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))

def test_Delete_Inventory(app, client): 
    ##Tests to see if row will delete from db
    del app
    res = client.get('/Inventory/del_Inventory/iPhone Screen') 
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


