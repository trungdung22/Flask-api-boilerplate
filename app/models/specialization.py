# coding: utf-8
from .base import BaseModel, db, relationship
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy


class Specialization(BaseModel):
    __tablename__ = 'specialization'

    title_lang = relationship(
        "SpecDescriptionLang",
        collection_class=attribute_mapped_collection("lang_code"),
    )

    title_map = association_proxy(
        'title_lang', 'value',
        creator=lambda k, v: SpecDescriptionLang(lang_code=k, value=v),
    )
    code = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.code


class SpecDescriptionLang(BaseModel):
    __tablename__ = 'spec_title_lang'
    value = db.Column(db.String())
    lang_code = db.Column(db.String(20))  # for ex: 'en', 'fr', 'de', 'ru'
    specialization_id = db.Column(db.Integer, db.ForeignKey('specialization.id'))