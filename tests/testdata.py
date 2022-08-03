from app.models.user import User as UserModel
from app.models.location import Location as LocationModel
from app.models.specialization import Specialization as SpecializationModel
from app.models.doctor import Doctor as DoctorModel
from app.models.keyword import LanguageCode


def seed_data():
    admin_user = UserModel(username="admin", email="dung.do@gmail.com", is_admin=True)
    admin_user.set_password("password123")
    admin_user.save()

    england_loc = LocationModel(code="en")
    england_loc.description_map = {
        LanguageCode.EN: "England location description.",
        LanguageCode.FR: "Description de l'emplacement en Angleterre."
    }
    england_loc.save()
    us_loc = LocationModel(code="us")
    us_loc.description_map = {
        LanguageCode.EN: "United state location description.",
        LanguageCode.FR: "Description de l'emplacement aux États-Unis."
    }
    us_loc.save()
    vietnam_loc = LocationModel(code="vn")

    vietnam_loc.description_map = {
        LanguageCode.EN: "Vietname state location description.",
        LanguageCode.FR: "Description de l'emplacement de l'État vietnamien."
    }
    vietnam_loc.save()

    spec1 = SpecializationModel(code="allergy")
    spec1.title_map = {
        LanguageCode.EN: "allergy",
        LanguageCode.FR: "allergie"
    }
    spec2 = SpecializationModel(code="immunology")
    spec2.title_map = {
        LanguageCode.EN: "immunology",
        LanguageCode.FR: "immunologie"
    }
    spec3 = SpecializationModel(code="anesthesiology")
    spec3.title_map = {
        LanguageCode.EN: "anesthesiology",
        LanguageCode.FR: "anesthésiologie"
    }
    spec4 = SpecializationModel(code="dermatology")
    spec4.title_map = {
        LanguageCode.EN: "dermatology",
        LanguageCode.FR: "dermatologie"
    }
    spec5 = SpecializationModel(code="diagnostic")
    spec5.title_map = {
        LanguageCode.EN: "diagnostic",
        LanguageCode.FR: "diagnostique"
    }
    spec1.save()
    spec2.save()
    spec3.save()
    spec4.save()
    spec5.save()

    doctor_1 = DoctorModel(name="Jillie Annika",
                           price=1000.0,
                           location_id=vietnam_loc.id)
    doctor_1.description_map = {
        LanguageCode.EN: "By filling out the needed information on the website, you can now make a fake medical prescription.",
        LanguageCode.FR: "En remplissant les informations nécessaires sur le site Web, vous pouvez désormais faire une fausse ordonnance médicale."
    }
    doctor_1.add_spec(spec1)
    doctor_1.add_spec(spec2)
    doctor_1.save()

    doctor_2 = DoctorModel(name="Alf Ellery",
                           price=2000.0,
                           location_id=england_loc.id)
    doctor_2.description_map = {
        LanguageCode.EN: "By filling out the needed information on the website, you can now make a fake medical prescription.",
        LanguageCode.FR: "En remplissant les informations nécessaires sur le site Web, vous pouvez désormais faire une fausse ordonnance médicale."
    }
    doctor_2.add_spec(spec2)
    doctor_2.add_spec(spec4)
    doctor_2.save()

