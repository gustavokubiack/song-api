from authentication.serializers import UserSerializer
import pytest


@pytest.mark.django_db
def test_create_user_should_return_a_new_user():
    user_data = {
        "username": "username",
        "password": "password",
        "email": "email@domain.com",
    }
    creator = UserSerializer()
    user = creator.create(user_data)
    assert user.username == "username"
    assert user.email == "email@domain.com"
