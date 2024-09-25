from rest_framework.reverse import reverse
import pytest


@pytest.mark.django_db
def test_song_list_should_return_serialized_data(auth_client, song):
    url = reverse("songs-create-list")
    response = auth_client.get(url)
    assert response.status_code == 200
    assert "Artist 1" in response.data["results"][0]["artists"][0]["name"]


@pytest.mark.django_db
def test_song_create_should_use_only_ids(auth_client, artist, genre, user):
    url = reverse("songs-create-list")
    response = auth_client.post(
        url,
        {
            "title": "title",
            "artists": [artist.id],
            "genre": genre.id,
            "stars": 5,
            "user": user.id,
        },
    )

    assert response.status_code == 201
