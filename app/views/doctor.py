# -*- coding: utf-8 -*-
from flask import request
from app.middlerwares.token_required import token_required
from app.config.exceptions import InvalidDataException
from app.config.routers import doctor_namespace
import app.utils.helpers.swagger.models.doctor as doctor_swagger
from app.models.validators.doctor import (
    DoctorCreate as DoctorCreateValidator,
)
from app.models.serializers.doctor import DoctorSchema
from marshmallow import (
    ValidationError,
)
from app.models.doctor import Doctor as DoctorModel
from app.models.location import Location as LocationModel
from app.models.specialization import Specialization as SpecializationModel
from .base import BaseResource


@doctor_namespace.route("")
class DoctorListResource(BaseResource):

    @doctor_namespace.doc(
        "Doctor list",
        parser=doctor_swagger.doctor_list_params,
        responses={
            200: ("doctors data", doctor_swagger.doctor_list_response),
            401: "Unauthorized exception."
        },
    )
    @token_required
    def get(self):
        args = request.args
        spec_filter = args.get("spec", None)
        location_filter = args.get("location", None)
        doctor_schemas = DoctorSchema(many=True)
        qs = DoctorModel.query

        if spec_filter:
            qs = qs.filter(DoctorModel.spec_list.any(SpecializationModel.title == spec_filter))
        if location_filter:
            qs = qs.join(DoctorModel.location).filter(LocationModel.name == location_filter)

        data, meta = self.paginate_resource(qs)
        response_data = {
            "data": doctor_schemas.dump(data),
            "meta": meta
        }
        return self.response_success(data=response_data)

    @doctor_namespace.expect(doctor_swagger.doctor_model)
    @doctor_namespace.doc(
        "Doctor create",
        responses={
            201: ("Doctor created", doctor_swagger.doctor_create_success),
            422: "Validations failed."
        },
    )
    @token_required
    def post(self):
        """ Endpoint to create the doctor """
        payload = request.get_json()
        try:
            validator = DoctorCreateValidator()
            doctor_data = validator.load(data=payload)
        except ValidationError as err:
            raise InvalidDataException(message=err.messages)

        spec_list = doctor_data.pop("spec_list")
        location_name = doctor_data.pop("location")
        location = LocationModel.query.filter_by(name=location_name).first()

        spec_objs = []
        for spec_title in spec_list:
            spec = SpecializationModel.query.filter_by(title=spec_title).first()
            spec_objs.append(spec)
        doctor = DoctorModel(**doctor_data)
        for spec_obj in spec_objs:
            doctor.add_spec(spec_obj)
        doctor.location = location
        doctor.save()
        return self.response_success(message="doctor created successfully", code=201)


@doctor_namespace.route('/<int:doctor_id>')
class DoctorResource(BaseResource):
    """" Resource class for single doctor endpoints """

    @doctor_namespace.doc(
        "Doctor detail",
        responses={
            200: ("doctor data", doctor_swagger.doctor_data),
            401: "Unauthorized exception."
        },
    )
    @token_required
    def get(self, doctor_id):
        """ Endpoint to get a single doctor """

        doctor_schema = DoctorSchema()
        doctor = doctor_schema.dump(DoctorModel.find_by_id(doctor_id))
        return self.response_success(data=doctor)
