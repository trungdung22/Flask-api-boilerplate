""" Module for Category Model """

from .base import BaseModel, db


class Location(BaseModel):
    """ Category Model class """

    __tablename__ = 'location'

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
