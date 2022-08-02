""" Module for Category Model """

from .base import BaseModel, db, relationship

spec_assoc = db.Table("spec_assoc",
                     db.Column("specialization_id", db.Integer, db.ForeignKey("specialization.id")),
                     db.Column("doctor_id", db.Integer, db.ForeignKey("doctor.id")))


class Doctor(BaseModel):
    """ Category Model class """

    __tablename__ = 'doctor'

    name = db.Column(db.String(100),  nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.DECIMAL(12, 2), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = relationship('Location', backref=db.backref('doctors'), lazy="joined")
    spec_list = relationship('Specialization', secondary=spec_assoc, lazy="joined")

    def add_spec(self, spec):
        if spec not in self.spec_list:
            self.spec_list.append(spec)
            return True
        return False

    def remove_spec(self, spec):
        if spec in self.tagList:
            self.spec_list.remove(spec)
            return True
        return False
