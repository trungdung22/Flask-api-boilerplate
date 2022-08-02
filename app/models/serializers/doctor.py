from .base import BaseSchema
from marshmallow import fields, post_dump, pre_dump
from app.utils.utility import get_lang_code


class LocationSchema(BaseSchema):
    """ Doctor Schema Class """
    name = fields.String(required=True)
    description = fields.String(required=True)

    class Meta:
        strict = True

    @pre_dump
    def pre_dump(self, obj, **kwargs):
        lang_code = get_lang_code()
        setattr(obj, "description", obj.description_map.get(lang_code))
        return obj


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
