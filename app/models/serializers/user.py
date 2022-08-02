""" Module for the User Schema """

from marshmallow import fields
from .base import BaseSchema, Schema


class UserSchema(BaseSchema):
    """ User Schema Class """
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=False , load_only=True)
    is_admin = fields.Boolean(required=True)

    class Meta:
        strict = True


class UserLoginSchema(Schema):
    token = fields.String(required=True, load_only=True)