from marshmallow import (
    Schema,
    fields,
    validate
)


class UserSignup(Schema):
    username = fields.Str(
        required=True
    )
    is_admin = fields.Boolean(
        required=True
    )
    email = fields.Str(
        required=True, validate=validate.Email(error="Not a valid email address")
    )
    password = fields.Str(
        required=True, validate=[validate.Length(min=6, max=36)], load_only=True
    )


class UserLogin(Schema):
    username = fields.Str(
        required=True
    )
    password = fields.Str(
        required=True, load_only=True
    )
