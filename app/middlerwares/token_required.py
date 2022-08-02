""" Module for auth token validation """

import os
from functools import wraps
import jwt
from flask import request
from app.config.exceptions import UnauthorizedException


def token_required(f):
    """ Authentication decorator. Validates token from the client

        Args:
            f (function): Function to be decorated
        Returns:
            decorated (function): Decorated function
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            message = 'No authorization token provided'
            raise UnauthorizedException(message=message)

        try:
            decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
        except Exception:
            message = 'The provided authorization token is invalid'
            raise UnauthorizedException(message=message)
        setattr(request, 'decoded_token', decoded_token)
        return f(*args, **kwargs)
    return decorated
