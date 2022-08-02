""" Module for Category Model """

from .base import BaseModel, db, relationship
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy


class Location(BaseModel):
    """ Category Model class """

    __tablename__ = 'location'

    code = db.Column(db.String(100), unique=True, nullable=False)
    description_assoc = relationship(
        "LocationDescription",
        collection_class=attribute_mapped_collection("lang_code"),
    )

    description_map = association_proxy(
        'description_assoc', 'value',
        creator=lambda k, v: LocationDescription(lang_code=k, value=v),
    )

    lang_code = association_proxy(
        "description_assoc", "lang_code"
    )


class LocationDescription(BaseModel):
    __tablename__ = 'location_description'
    value = db.Column(db.Text())
    lang_code = db.Column(db.String(20))  # for ex: 'en', 'fr', 'de', 'ru'
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))


