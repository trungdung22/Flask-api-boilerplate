import pytest
from flask.testing import FlaskClient
from app.config.server import application
from app.config.plugins import db as _db
from .testdata import seed_data


pytest_plugins = ['tests.fixtures.auth',]


def urls(current_app):
    """Display all of the url matching routes for the project.

    Borrowed from Flask-Script, converted to use Click.
    """
    rows = []
    column_headers = ('Rule', 'Endpoint', 'Arguments')

    rules = current_app.url_map.iter_rules()
    for rule in rules:
        rows.append((rule.rule, rule.endpoint, None))
    column_length = 2

    str_template = ''
    table_width = 0

    if column_length >= 1:
        max_rule_length = max(len(r[0]) for r in rows)
        max_rule_length = max_rule_length if max_rule_length > 4 else 4
        str_template += '{:' + str(max_rule_length) + '}'
        table_width += max_rule_length

    if column_length >= 2:
        max_endpoint_length = max(len(str(r[1])) for r in rows)
        max_endpoint_length = (
            max_endpoint_length if max_endpoint_length > 8 else 8)
        str_template += '  {:' + str(max_endpoint_length) + '}'
        table_width += 2 + max_endpoint_length

    if column_length >= 3:
        max_arguments_length = max(len(str(r[2])) for r in rows)
        max_arguments_length = (
            max_arguments_length if max_arguments_length > 9 else 9)
        str_template += '  {:' + str(max_arguments_length) + '}'
        table_width += 2 + max_arguments_length

    print(str_template.format(*column_headers[:column_length]))
    print('-' * table_width)

    for row in rows:
        print(str_template.format(*row[:column_length]))


@pytest.fixture(scope='module')
def app():
    import app.views.doctor
    import app.views.user
    """An application for the tests."""
    _app = application

    with _app.app_context():
        _db.create_all()
        seed_data()
        urls(_app)

    ctx = _app.test_request_context()
    ctx.push()

    yield _app
    _db.session.close()
    _db.drop_all()
    ctx.pop()


class TestClient(FlaskClient):
    def open(self, *args, **kwargs):
        custom_headers = {
            'Content-Type': 'application/json'
        }
        headers = kwargs.pop('headers', {})
        headers.update(custom_headers)
        kwargs['headers'] = headers
        return super(TestClient, self).open(*args, **kwargs)


@pytest.fixture(scope='module')
def client(app):
    app.test_client_class = TestClient
    return app.test_client()


@pytest.fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()
    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()

