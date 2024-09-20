from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from songs.models import Song
from artists.models import Artist
from genres.models import Genre, GenreTypeChoices
from reviews.models import Review
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


@fixture
def genre(db):
    genre_instance = Genre.objects.create(name=GenreTypeChoices.BLUES)
    return genre_instance


@fixture
def artists(db):
    artist_list = []
    for i in range(5):
        artist = Artist.objects.create(name=f"Artist {i + 1}")
        artist_list.append(artist)
    return artist_list


@fixture
def song(db, genre, artists):
    song_instance = Song.objects.create(
        title="Test Song",
        genre=genre,
        release_date="2023-01-01",
        resume="A test song for unit testing.",
    )
    song_instance.artists.set(artists)
    return song_instance


@fixture
def review(db, song):
    review_instance = Review.objects.create(
        song=song,
        comment="Good",
        stars=5,
    )
    return review_instance
