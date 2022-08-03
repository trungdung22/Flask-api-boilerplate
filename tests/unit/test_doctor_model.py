from app.models.user import User as UserModel
from app.models.location import Location as LocationModel
from app.models.specialization import Specialization as SpecializationModel
from app.models.doctor import Doctor as DoctorModel
import pytest
from app.models.keyword import LanguageCode


@pytest.mark.usefixtures('db')
class TestSpec:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get spec by ID."""
        loc = LocationModel(code="location1",
                            description_map={
                                LanguageCode.FR: "vn locations",
                                LanguageCode.EN: "fra translates vn locations"
                            })
        loc.save()

        spec = SpecializationModel(code="spec1")
        spec.title_map = {
            LanguageCode.EN: "immunology",
            LanguageCode.FR: "immunologie"
        }
        spec.save()

        doctor_1 = DoctorModel(name="doctor name 1",
                               price=1000.0, location_id=loc.id)
        doctor_1.description_map = {
            LanguageCode.EN: "By filling out the needed information on the website, you can now make a fake medical prescription.",
            LanguageCode.FR: "En remplissant les informations nécessaires sur le site Web, vous pouvez désormais faire une fausse ordonnance médicale."
        }
        doctor_1.add_spec(spec)
        doctor_1.save()
        retrieved = DoctorModel.find_by_id(doctor_1.id)
        assert retrieved.id == doctor_1.id
        assert retrieved.location_id == doctor_1.location_id
        assert retrieved.spec_list == doctor_1.spec_list
