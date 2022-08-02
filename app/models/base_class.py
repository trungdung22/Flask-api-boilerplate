# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.base import BaseModel  # noqa
from app.models.doctor import Doctor, spec_assoc  # noqa
from app.models.location import Location, LocationKeywordDescriptionAssociation  # noqa
from app.models.specialization import Specialization  # noqa
from app.models.keyword import KeywordText, KeywordString # noqa