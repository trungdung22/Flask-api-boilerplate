""" Module for authorization fixture """
from app.models.user import User as UserModel
from app.models.serializers.user import UserSchema


def admin_auth_header():
    """ Admin auth header fixture """

    user = UserModel.query.filter_by(username="adminuser").first()
    user_schema = UserSchema(exclude=['password'])
    logged_in_user = user_schema.dump(user)
    token = UserModel.generate_auth_token(logged_in_user)

    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
