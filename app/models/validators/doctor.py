from marshmallow import (
    Schema,
    fields,
)


class DoctorCreate(Schema):
    name = fields.Str(
        required=True,
    )
    description = fields.Str(
        required=True
    )
    price = fields.Decimal(
        required=True
    )
    location = fields.Str(
        required=True
    )
    spec_list = fields.List(fields.Str(), required=True)
