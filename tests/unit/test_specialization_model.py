from app.models.specialization import Specialization as SpecializationModel
from app.models.keyword import LanguageCode
import pytest


@pytest.mark.usefixtures('db')
class TestSpec:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get spec by ID."""
        spec = SpecializationModel(code="spec1")
        spec.title_map = {
            LanguageCode.EN: "immunology",
            LanguageCode.FR: "immunologie"
        }
        spec.save()

        retrieved = SpecializationModel.find_by_id(spec.id)
        assert retrieved.id == spec.id
