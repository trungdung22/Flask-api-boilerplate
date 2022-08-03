# -*- coding: utf-8 -*-
import datetime
from app.config.plugins import bcrypt
from .base import BaseModel, db
import jwt
import os
from dotenv import load_dotenv

load_dotenv()


class User(BaseModel):
    """ User Model for storing user related details """
    __tablename__ = "users"

    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        self.registered_on = datetime.datetime.utcnow()
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password_hash, value)

    @classmethod
    def generate_auth_token(cls, user):
        """
        Generates the authentication token
        Args:
            user(dict): user data

        Returns:
            token(str): Json Web Token
        """

        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'user': user
        }
        token = jwt.encode(
            payload,
            os.getenv('SECRET_KEY'),
            algorithm='HS256'
        )
        if not isinstance(token, str):
            token = token.decode('UTF-8')
        return token

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)
