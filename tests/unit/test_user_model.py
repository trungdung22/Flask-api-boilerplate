from app.models.user import User as UserModel
import pytest


@pytest.mark.usefixtures('db')
class TestUser:
    """User tests."""

    def test_create_get_by_id_success(self):
        """Get user by ID."""
        user = UserModel(username="user1", email="user1@gmail.com", is_admin=True)
        user.set_password("password123")
        user.save()

        retrieved = UserModel.find_by_id(user.id)
        assert retrieved.id == user.id

    def test_check_password(self):
        """Check password."""
        user = UserModel(username='foo', email='foo@bar.com')
        user.set_password("password123")
        user.save()
        assert user.check_password('password123')
        assert not user.check_password('barfoobaz')
