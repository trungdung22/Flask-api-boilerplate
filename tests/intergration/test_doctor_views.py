import pytest
from tests.fixtures.auth import admin_auth_header
import json


@pytest.mark.parametrize(
    'location,specialization',
    [(
            'vn',
            'allergy',
    )]
)
def test_doctor_get_by_loc_and_spec(client, location, specialization):
    data = {
        'spec': specialization,
        'location': location
    }
    token_header = admin_auth_header()
    url = '/api/v1/doctors'
    rv = client.get(url, query_string=data, headers=token_header)
    data = rv.json
    assert rv.status_code == 200
    assert 'result' in data
    results = data['result']['data']
    assert len(results) > 0


@pytest.mark.parametrize(
    'specialization,language',
    [(
            'allergy',
            'fr',
    )]
)
def test_doctor_get_by_language(client, specialization, language):
    data = {
        'spec': specialization,
        'lang_code': language
    }
    token_header = admin_auth_header()
    url = '/api/v1/doctors'
    rv = client.get(url, query_string=data, headers=token_header)
    data = rv.json
    assert rv.status_code == 200
    assert 'result' in data
    results = data['result']['data']
    assert len(results) > 0
    print(results)
    spec = results[0]["spec_list"][0]["title"]
    assert spec == "allergie"


def test_create_doctor_success(client):
    data = {
        "name": "John Snow",
        "description": {
            "en": "By filling out the needed information on the website, you can now make a fake medical prescription.",
            "fr": "En remplissant les informations nécessaires sur le site Web, vous pouvez désormais faire une fausse ordonnance médicale."
        },
        "location": "en",
        "price": 3000,
        "spec_list": [
            "anesthesiology",
            "dermatology"
        ]
    }
    token_header = admin_auth_header()
    token_header['accept'] = "application/json"
    url = '/api/v1/doctors'
    rv = client.post(url, data=json.dumps(data), headers=token_header)
    print(rv)
    data = rv.json
    assert rv.status_code == 201
    assert data["status"] == "success"


def test_create_doctor_no_auth_failed(client):
    data = {
        "name": "John Snow",
        "description": {
            "en": "By filling out the needed information on the website, you can now make a fake medical prescription.",
            "fr": "En remplissant les informations nécessaires sur le site Web, vous pouvez désormais faire une fausse ordonnance médicale."
        },
        "location": "en",
        "price": 3000,
        "spec_list": [
            "anesthesiology",
            "dermatology"
        ]
    }
    url = '/api/v1/doctors'
    rv = client.post(url, data=json.dumps(data))
    assert rv.status_code == 500


@pytest.mark.parametrize(
    'location,specialization',
    [(
            'vn',
            'allergy',
    )]
)
def test_doctor_get_without_auth(client, location, specialization):
    data = {
        'spec': specialization,
        'location': location
    }
    url = '/api/v1/doctors'
    rv = client.get(url, query_string=data)
    assert rv.status_code == 500
