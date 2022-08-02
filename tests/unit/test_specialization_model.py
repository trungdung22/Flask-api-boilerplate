from app.models.specialization import Specialization as SpecializationModel
import pytest


@pytest.mark.usefixtures('db')
class TestSpec:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get spec by ID."""
        spec = SpecializationModel(title="spec1")
        spec.save()

        retrieved = SpecializationModel.find_by_id(spec.id)
        assert retrieved.id == spec.id
