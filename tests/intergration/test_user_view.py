import json


def test_user_login_success(client):
    data = {
          "username": "dung.do@gmail.com",
          "password": "password123"
    }
    url = '/api/v1/users/login'
    rv = client.post(url, data=json.dumps(data))
    data = rv.json
    assert rv.status_code == 200
    assert "token" in data

