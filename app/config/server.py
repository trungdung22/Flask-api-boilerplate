""" Module for Server configuration """
from flask import Flask, Blueprint
from flask_restx import Api
from app.config.exceptions import (
    ItemNotFoundException,
    UnauthorizedException,
    ForbiddenException,
    ServerErrorException,
    InvalidDataException
)
from app.config.plugins import bcrypt, cache, db, migrate, cors
from app.config.environment import AppConfig
from app.config import commands


api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api/v1')

authorizations = {
    'Token Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
api = Api(
    api_blueprint,
    title='Arrows Shop API',
    description='Online shopping API',
    security='Token Auth',
    doc='/documentation',
    authorizations=authorizations)


def create_app(config_object=AppConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    # cors.init_app(api_blueprint, origins=origins)
    app.register_blueprint(api_blueprint)


def register_errorhandlers(app):

    def error_handler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(ItemNotFoundException)(error_handler)
    app.errorhandler(UnauthorizedException)(error_handler)
    app.errorhandler(ForbiddenException)(error_handler)
    app.errorhandler(ServerErrorException)(error_handler)
    app.errorhandler(InvalidDataException)(error_handler)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.seed)
    app.cli.add_command(commands.migrate)
    app.cli.add_command(commands.drop_all)
    app.cli.add_command(commands.urls)
    app.cli.add_command(commands.test)


application = create_app()
