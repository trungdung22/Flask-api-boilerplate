from app.models.location import Location as LocationModel
from app.models.keyword import LanguageCode
import pytest


@pytest.mark.usefixtures('db')
class TestLocation:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get location by ID."""
        loc = LocationModel(name="location1",
                            description={
                                   LanguageCode.ENG: "vn locations",
                                   LanguageCode.FRA: "fra translates vn locations"
                            })
        loc.save()

        retrieved = LocationModel.find_by_id(loc.id)
        print(retrieved.description)
        assert retrieved.id == loc.id
