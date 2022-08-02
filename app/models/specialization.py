# coding: utf-8
from .base import BaseModel, db


class Specialization(BaseModel):
    __tablename__ = 'specialization'

    title = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.title
