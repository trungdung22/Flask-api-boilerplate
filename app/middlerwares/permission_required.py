# -*- coding: utf-8 -*-
""" Module for permission validation """

from functools import wraps
from flask import request
from app.models.user import User
from app.config.exceptions import ForbiddenException


def permission_required(f):
    """ Permission decorator. Validates user if is allowed to perform action

        Args:
            f (function): Function to be decorated
        Returns:
            decorated (function): Decorated function
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        decoded_token = request.decoded_token
        current_user = User.find_by_id(decoded_token['user']['id'])

        if not current_user.is_admin:
            message = 'Permission denied. You are not authorized to perform this action'
            raise ForbiddenException(message=message)

        return f(*args, **kwargs)
    return decorated
