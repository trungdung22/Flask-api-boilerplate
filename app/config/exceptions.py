from flask import jsonify


class Base(Exception):
    status_code = 500
    message = ""

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def build_msg(self):
        return {'msg': self.message}

    def to_json(self):
        rv = self.build_msg()
        return jsonify(rv)


class ItemNotFoundException(Base):
    status_code = 404


class UnauthorizedException(Base):
    status_code = 401


class ForbiddenException(Base):
    status_code = 403


class ServerErrorException(Base):
    status_code = 500


class InvalidPasswordException(Base):
    status_code = 403


class InvalidDataException(Base):
    status_code = 422
