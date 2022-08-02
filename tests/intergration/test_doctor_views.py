import pytest
from tests.fixtures.auth import admin_auth_header


@pytest.mark.parametrize(
    'location,specialization',
    [(
        'vn',
        'allergy',
    )]
)
def test_doctor_get(client, location, specialization):
    data = {
        'spec': specialization,
        'location': location
    }
    token_header = admin_auth_header()
    url = '/api/v1/doctors'
    rv = client.get(url, query_string=data, headers=token_header)
    data = rv.json
    print(data)
    assert rv.status_code == 200
    assert 'result' in data
    results = data['result']['data']
    assert len(results) > 0


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
    print(rv)
    assert rv.status_code == 500
