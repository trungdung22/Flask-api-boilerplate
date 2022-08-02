from app.models.user import User as UserModel
from app.models.location import Location as LocationModel
from app.models.specialization import Specialization as SpecializationModel
from app.models.doctor import Doctor as DoctorModel
import pytest


@pytest.mark.usefixtures('db')
class TestSpec:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get spec by ID."""
        england_loc = LocationModel(name="england2", description="england locations")
        england_loc.save()
        spec1 = SpecializationModel(title="allerg2y")
        spec1.save()
        spec2 = SpecializationModel(title="immunology2")
        spec2.save()

        doctor_1 = DoctorModel(name="doctor name 1", description="doctor description 1",
                               price=1000.0, location_id=england_loc.id)
        doctor_1.add_spec(spec1)
        doctor_1.add_spec(spec2)
        doctor_1.save()
        retrieved = DoctorModel.find_by_id(doctor_1.id)
        assert retrieved.id == doctor_1.id
        assert retrieved.location_id == doctor_1.location_id
        assert retrieved.spec_list == doctor_1.spec_list
