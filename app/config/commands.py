# -*- coding: utf-8 -*-
"""Click commands."""
import click
from flask.cli import with_appcontext
from app.models.base import db
from app.models.user import User as UserModel
from app.models.location import Location as LocationModel
from app.models.specialization import Specialization as SpecializationModel
from app.models.doctor import Doctor as DoctorModel # noqa
from app.models.keyword import KeywordText, KeywordString, LanguageCode # noqa
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound
import os

HERE = os.path.abspath(os.path.dirname(__file__))
CONFIG_ROOT = os.path.join(HERE, os.pardir)
PROJECT_ROOT = os.path.join(CONFIG_ROOT, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')


@click.command()
def test():
    """Run the tests."""
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose', '-s', os.path.abspath(__file__)])
    exit(rv)


@click.command()
@with_appcontext
def migrate():
    db.create_all()


@click.command()
@with_appcontext
def drop_all():
    db.drop_all()


@click.command()
@with_appcontext
def seed():
    admin_user = UserModel(username="admin", email="dung.do@gmail.com", is_admin=True)
    admin_user.set_password("password123")
    admin_user.save()

    england_loc = LocationModel(name="england")
    england_loc.description_map = {
        LanguageCode.ENG: "England location description.",
        LanguageCode.FRA: "fra translates locations"
    }
    england_loc.save()
    us_loc = LocationModel(name="us")
    us_loc.description_map = {
        LanguageCode.ENG: "us locations",
        LanguageCode.FRA: "fra translates us locations"
    }
    us_loc.save()
    vietnam_loc = LocationModel(name="vn")

    vietnam_loc.description_map = {
        LanguageCode.ENG: "vn locations",
        LanguageCode.FRA: "fra translates vn locations"
    }
    vietnam_loc.save()

    spec1 = SpecializationModel(title="allergy")
    spec2 = SpecializationModel(title="immunology")
    spec3 = SpecializationModel(title="anesthesiology")
    spec4 = SpecializationModel(title="dermatology")
    spec5 = SpecializationModel(title="diagnostic")
    spec1.save()
    spec2.save()
    spec3.save()
    spec4.save()
    spec5.save()

    doctor_1 = DoctorModel(name="doctor name 1", description="doctor description 1",
                           price=1000.0, location_id=vietnam_loc.id)
    doctor_1.add_spec(spec1)
    doctor_1.add_spec(spec2)
    doctor_1.save()


@click.command()
@click.option('--url', default=None,
              help='Url to test (ex. /static/image.png)')
@click.option('--order', default='rule',
              help='Property on Rule to order by (default: rule)')
@with_appcontext
def urls(url, order):
    """Display all of the url matching routes for the project.

    Borrowed from Flask-Script, converted to use Click.
    """
    rows = []
    column_headers = ('Rule', 'Endpoint', 'Arguments')

    if url:
        try:
            rule, arguments = (
                current_app.url_map.bind('localhost')
                .match(url, return_rule=True))
            rows.append((rule.rule, rule.endpoint, arguments))
            column_length = 3
        except (NotFound, MethodNotAllowed) as e:
            rows.append(('<{}>'.format(e), None, None))
            column_length = 1
    else:
        rules = sorted(
            current_app.url_map.iter_rules(),
            key=lambda rule: getattr(rule, order))
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

    click.echo(str_template.format(*column_headers[:column_length]))
    click.echo('-' * table_width)

    for row in rows:
        click.echo(str_template.format(*row[:column_length]))
