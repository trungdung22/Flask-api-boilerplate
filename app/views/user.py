# -*- coding: utf-8 -*-
from flask import request
from app.middlerwares.token_required import token_required
from app.config.routers import user_namespace
import app.utils.helpers.swagger.models.user as userSwagger
from app.models.validators.user import (
    UserLogin as UserLoginValidator,
    UserSignup as UserSignupValidator
)
from app.config.exceptions import (
    InvalidDataException,
    ItemNotFoundException,
    InvalidPasswordException
)
from app.models.serializers.user import UserSchema
from marshmallow import (
    ValidationError,
)
from app.models.user import User as UserModel
from .base import BaseResource


@user_namespace.route('/signup')
class UserSignupResource(BaseResource):
    """" Resource class for user signup endpoint """

    @user_namespace.doc(
        "User signup resource",
        responses={
            201: ("User created", userSwagger.user_create_success),
            422: "Validations failed."
        },
    )
    @user_namespace.expect(userSwagger.signup_model)
    def post(self):
        """ Endpoint to create the user """
        payload = request.get_json()
        try:
            validator = UserSignupValidator()
            userdata = validator.load(data=payload)
        except ValidationError as err:
            raise InvalidDataException(message=err.messages)

        password = userdata.pop("password")
        new_user = UserModel(**userdata)
        new_user.set_password(password)
        new_user.save()

        return self.response_success(message="User created")


@user_namespace.route('/login')
class UserLoginResource(BaseResource):
    """" Resource class for user login endpoint """

    @user_namespace.doc(
        "Auth login resource",
        responses={
            200: ("Logged in", userSwagger.auth_success),
            422: "Validations input data failed.",
            403: "Incorrect password or incomplete credentials.",
            404: "Email does not match any account.",
        },
    )
    @user_namespace.expect(userSwagger.login_model)
    def post(self):
        """ Endpoint to login the user """

        payload = request.get_json()
        try:
            validator = UserLoginValidator()
            validator.load(data=payload)
        except ValidationError as err:
            return InvalidDataException(message=err.messages)

        email = payload['username']
        password = payload['password']
        user = UserModel.query.filter(UserModel.email == email).first()

        if user:
            if user.check_password(password):
                user_schema = UserSchema(exclude=['password'])
                logged_in_user = user_schema.dump(user)
                token = UserModel.generate_auth_token(logged_in_user)
                return {"token": token}, 200
            else:
                raise InvalidPasswordException(message="Incorrect password or incomplete credentials.")
        raise ItemNotFoundException(message="Email does not match any account.")


@user_namespace.route("")
class UserListResource(BaseResource):
    """ Resource class for User List endpoint """

    @user_namespace.doc(
        "User list resource",
        responses={
            200: ("uses data", userSwagger.user_list_success),
            401: "Unauthorized exception",
        },
    )
    @token_required
    def get(self):
        """ Endpoint to fetch user list """
        user_schemas = UserSchema(many=True)
        data, meta = self.paginate_resource(UserModel.query)
        response_data = {
            "data": user_schemas.dump(data),
            "meta": meta
        }
        return self.response_success(response_data)

