from .base import BaseModel, db


class LanguageCode:
    EN = "en"
    FR = "fr"


class LocationCode:
    ENGLAND = "england"
    US = "us"
    VIETNAM = "VIETNAM"


class SpecializationCode:
    ALLERGY = "allergy"
    IMMUNOLOGY = "immunology"
    ANESTHESIOLOGY = "anesthesiology"
    DERMATOLOGY = "dermatology"
    DIAGNOSTIC = "diagnostic"


class KeywordString(BaseModel):
    __tablename__ = "keyword_string"

    keyword = db.Column(db.String(100),  nullable=False)


class KeywordText(BaseModel):
    __tablename__ = "keyword_text"

    keyword = db.Column(db.Text, nullable=True)
