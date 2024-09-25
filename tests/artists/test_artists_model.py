from artists.models import Artist
import pytest


@pytest.mark.django_db
def test_artist_creation():
    artist = Artist.objects.create(
        name="John",
        birthday="1990-01-01",
        nationality="USA",
    )
    assert str(artist) == "John"
