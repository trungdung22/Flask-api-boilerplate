from marshmallow import (
    Schema,
    fields,
)


class DoctorDescription(Schema):
    en = fields.Str(
        required=True,
    )

    fr = fields.Str(
        required=True,
    )


class DoctorCreate(Schema):
    name = fields.Str(
        required=True,
    )
    description = fields.Nested(DoctorDescription(), required=True)

    price = fields.Decimal(
        required=True
    )

    location = fields.Str(
        required=True
    )

    spec_list = fields.List(fields.Str(), required=True)
