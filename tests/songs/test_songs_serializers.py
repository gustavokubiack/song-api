from django.utils.translation import gettext_lazy as _
from songs.serializers import SongModelSerializer, SongDetailSerializer
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
def test_valid_release_date_should_be_returned(artists, genre):
    serializer = SongModelSerializer(
        data={
            "title": "title",
            "artists": [artist.id for artist in artists],
            "genre": genre.id,
            "release_date": "2000-10-10",
        }
    )
    assert serializer.is_valid()
    release_date = serializer.validated_data["release_date"]
    assert release_date == date(2000, 10, 10)


@pytest.mark.django_db
def test_valid_release_date_should_validate(artists, genre):
    artist_data = [artist.id for artist in artists]
    serializer = SongDetailSerializer(
        data={
            "title": "title",
            "artists": artist_data,
            "genre": genre.id,
            "release_date": "1960-10-10",
        }
    )
    assert serializer.is_valid()
    release_date = serializer.validated_data["release_date"]
    assert release_date > date(1950, 1, 1)


@pytest.mark.django_db
def test_song_with_reviews_should_return_two_dot_five_rate(song, reviews):
    serializer = SongDetailSerializer(song)
    assert serializer.data["rate"] == 2.5


@pytest.mark.django_db
def test_song_without_reviews_should_return_none_rate(song):
    serializer = SongDetailSerializer(song)
    assert serializer.data["rate"] is None
