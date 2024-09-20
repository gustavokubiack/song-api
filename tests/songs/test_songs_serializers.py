from django.utils.translation import gettext_lazy as _
from songs.serializers import SongModelSerializer
import pytest
from datetime import date


@pytest.mark.django_db
def test_invalid_release_date_should_raise_validation_error(artists, genre):
    serializer = SongModelSerializer(
        data={
            "title": "title",
            "artists": [artists],
            "genre": genre,
            "release_date": "1900-10-10",
        }
    )
    assert not serializer.is_valid()
    assert "release_date" in serializer.errors
    assert serializer.errors["release_date"] == [
        _("Release Date cannot be less than 1950")
    ]


@pytest.mark.django_db
def test_valid_release_date_should_validate(artists, genre):
    artist_ids = list(map(lambda artist: artist.id, artists))
    serializer = SongModelSerializer(
        data={
            "title": "title",
            "artists": artist_ids,
            "genre": genre.id,
            "release_date": "1960-10-10",
        }
    )
    assert serializer.is_valid()
    release_date = serializer.validated_data["release_date"]
    assert release_date > date(1950, 1, 1)
