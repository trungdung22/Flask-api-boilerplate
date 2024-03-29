""" Module for Swagger doctor models """

from flask_restx import fields, reqparse
from app.config.routers import (doctor_namespace)

doctor_description_attr = doctor_namespace.model("Doctor description attr", {
    "en": fields.String,
    "fr": fields.String,
})

doctor_model = doctor_namespace.model('Doctor', {
    'name': fields.String(required=True, description='Doctor Name'),
    'description': fields.Nested(doctor_description_attr, required=True, description='Doctor description'),
    'location': fields.String(required=True, description='Location description'),
    'price': fields.Float(),
    'spec_list': fields.List(fields.String(), required=True, description="Doctor specialization"),
})

doctor_list_params = reqparse.RequestParser()
doctor_list_params.add_argument('spec', type=str, help='specialization')
doctor_list_params.add_argument('location', type=str, help='location')
doctor_list_params.add_argument('lower_price', type=float, help='lower price range')
doctor_list_params.add_argument('upper_price', type=float, help='upper price range')
doctor_list_params.add_argument('lang_code', type=str, help='language code en/fr')

doctor_detail_params = reqparse.RequestParser()
doctor_list_params.add_argument('lang_code', type=str, help='language code en/fr')

# response model
doctor_create_success = doctor_namespace.model("Doctor create success response", {
    "status": fields.Boolean,
    "message": fields.String,
})

location_data = doctor_namespace.model("Location data", {
    "id": fields.Integer,
    "name": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime
})

specialization_data = doctor_namespace.model("Specialization data", {
    "id": fields.Integer,
    "title": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime
})

doctor_data = doctor_namespace.model("Doctor data", {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "location": fields.Nested(location_data),
    "spec_list": fields.List(fields.Nested(specialization_data)),
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime
})

doctor_list_response = doctor_namespace.model("Doctor List reponse data", {
    "status": fields.String,
    "message": fields.String,
    "data": fields.List(fields.Nested(doctor_data))
})
