from rest_framework.reverse import reverse
import pytest


@pytest.mark.django_db
def test_review_list_should_return_serialized_data(auth_client, reviews):
    url = reverse("review-create-list")
    response = auth_client.get(url)
    assert response.status_code == 200
    assert "is_superuser" in response.data["results"][0]["user"]


@pytest.mark.django_db
def test_review_create_should_use_only_ids(auth_client, song):
    url = reverse("review-create-list")
    response = auth_client.post(
        url,
        {
            "song": song.id,
            "artists": [1],
            "genre": 1,
            "stars": 5,
            "user": 1,
        },
    )

    assert response.status_code == 201
