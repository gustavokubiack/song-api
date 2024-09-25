from django.utils.translation import gettext_lazy as _
from reviews.serializers import ReviewSerializer, ReviewListSerializer
import pytest


@pytest.mark.django_db
def test_six_stars_should_raise_validation_error():
    serializer = ReviewSerializer(data={"stars": 6})
    assert not serializer.is_valid()
    assert "stars" in serializer.errors
    assert serializer.errors["stars"] == [_("Rating cannot be greater than 5")]


@pytest.mark.django_db
def test_zero_stars_should_raise_validation_error():
    serializer = ReviewSerializer(data={"stars": -1})
    assert not serializer.is_valid()
    assert "stars" in serializer.errors
    assert serializer.errors["stars"] == [_("Rating cannot be less than 0")]


@pytest.mark.django_db
def test_four_stars_should_validate(song, user):
    serializer = ReviewSerializer(data={"stars": 4, "song": song.id, "user": user.id})
    assert serializer.is_valid()
    assert serializer.validated_data["stars"] == 4
