from .base import BaseSchema
from marshmallow import fields


class LocationSchema(BaseSchema):
    """ Doctor Schema Class """
    name = fields.String(required=True)
    description = fields.String(required=True)

    class Meta:
        strict = True


class SpecializationSchema(BaseSchema):
    """ Doctor Schema Class """
    title = fields.String(required=True)

    class Meta:
        strict = True


class DoctorSchema(BaseSchema):
    """ Doctor Schema Class """
    name = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.String(required=False, load_only=True)
    location = fields.Nested(LocationSchema())
    spec_list = fields.Nested(SpecializationSchema, many=True)

    class Meta:
        strict = True
