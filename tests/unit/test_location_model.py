from app.models.location import Location as LocationModel
from app.models.keyword import LanguageCode
import pytest


@pytest.mark.usefixtures('db')
class TestLocation:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get location by ID."""
        loc = LocationModel(code="location1",
                            description_map={
                                   LanguageCode.FR: "vn locations",
                                   LanguageCode.EN: "fra translates vn locations"
                            })
        loc.save()

        retrieved = LocationModel.find_by_id(loc.id)
        assert retrieved.id == loc.id
