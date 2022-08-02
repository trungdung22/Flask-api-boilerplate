from app.models.user import User as UserModel
from app.models.location import Location as LocationModel
from app.models.specialization import Specialization as SpecializationModel
from app.models.doctor import Doctor as DoctorModel


def seed_data():
    admin_user = UserModel(username="adminuser", email="adminuser@gmail.com", is_admin=True)
    admin_user.set_password("password123")
    admin_user.save()

    england_loc = LocationModel(name="england", description="england locations")
    england_loc.save()
    us_loc = LocationModel(name="us", description="US locations")
    us_loc.save()
    vietnam_loc = LocationModel(name="vn", description="VN locations")
    vietnam_loc.save()

    spec1 = SpecializationModel(title="allergy")
    spec1.save()
    spec2 = SpecializationModel(title="immunology")
    spec2.save()
    spec3 = SpecializationModel(title="anesthesiology")
    spec3.save()
    spec4 = SpecializationModel(title="dermatology")
    spec4.save()
    spec5 = SpecializationModel(title="diagnostic")
    spec5.save()

    doctor_1 = DoctorModel(name="doctor name 1", description="doctor description 1",
                           price=1000.0, location_id=vietnam_loc.id)
    doctor_1.add_spec(spec1)
    doctor_1.add_spec(spec2)
    doctor_1.save()
