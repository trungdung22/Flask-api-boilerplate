from app.models.location import Location as LocationModel
import pytest


@pytest.mark.usefixtures('db')
class TestLocation:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get location by ID."""
        loc = LocationModel(name="location1", description="location description")
        loc.save()

        retrieved = LocationModel.find_by_id(loc.id)
        assert retrieved.id == loc.id
