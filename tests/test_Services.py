## Will be used to test the User related endpoints 
import json

def test_Insert(app, client): 
    ##Tests to see if data gets inserted into db
    del app
    res = client.get('Services/mk_Service/Screen Repair/repairs the screen/15.0')
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))

def test_Update(app, client): 
    ##Tests to see if data updates from db
    del app
    res = client.get('Services/update_Services/Screen Repair/repairs the screen/16.0')
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))



def test_Delete(app, client): 
    ##Tests to see if data deletes from db
    del app
    res = client.get('Services/del_Services/Screen Repair')
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

