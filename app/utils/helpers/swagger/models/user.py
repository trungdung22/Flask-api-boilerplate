""" Module for Swagger user models """

from flask_restx import fields
from app.config.routers import (user_namespace)

signup_model = user_namespace.model('Signup', {
    'username': fields.String(required=True, description='User Name'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
    'is_admin': fields.Boolean(required=True, description='Is Admin'),
})

login_model = user_namespace.model('Login', {
    'username': fields.String(required=True, description='User info'),
    'password': fields.String(required=True, description='User password')
})

user_create_success = user_namespace.model("Auth success response",{
    "status": fields.Boolean,
    "message": fields.String,
    "access_token": fields.String,
})

auth_success = user_namespace.model("Auth success response",{
    "status": fields.Boolean,
    "message": fields.String,
    "access_token": fields.String,
})

user_data = user_namespace.model("Auth success response",{
    "username": fields.String,
    "email": fields.String,
    "is_admin": fields.Boolean,
})

user_list_success = user_namespace.model("User list response",{
    "status": fields.Boolean,
    "message": fields.String,
    "data": fields.List(fields.Nested(user_data)),
})