from rest_framework import status
from rest_framework.reverse import reverse
from artists.models import Artist


def test_artist_list_create(auth_client):
    response = auth_client.post(
        reverse("artist-create-list"), {"name": "New Artist", "genre": "Rock"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Artist.objects.count() == 1
    assert Artist.objects.get().name == "New Artist"
