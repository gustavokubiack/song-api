from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from pytest import fixture


@fixture
def user(db):
    user = User.objects.create_user(
        username="user",
        password="password",
    )
    return user


@fixture
def client():
    client = APIClient()
    yield client


@fixture
def auth_client(client, user):
    response = client.post(
        reverse("token-obtain-pair"),
        {
            "username": user.username,
            "password": "password",
        },
    )
    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
    return client
