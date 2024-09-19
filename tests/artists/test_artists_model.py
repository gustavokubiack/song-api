from artists.models import Artist
from artists.choices import NationalityTypeChoices
import pytest


@pytest.mark.django_db
def test_artist_creation():
    artist = Artist.objects.create(
        name="John",
        birthday="1990-01-01",
        nacionality=NationalityTypeChoices.USA,
    )
    assert str(artist) == "John"
