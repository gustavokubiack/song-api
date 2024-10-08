from django.db.models import Avg
from django.utils.translation import gettext as _
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from songs.models import Song


class SongModelSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

    def validate_release_date(self, release_date):
        if release_date and release_date.year < 1950:
            raise serializers.ValidationError(
                _("Release Date cannot be less than 1950")
            )
        return release_date


class SongDetailSerializer(ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = ["id", "rate", "title", "release_date", "resume", "genre", "artists"]
        depth = 1

    def get_rate(self, obj: Song) -> float | None:
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return round(rate, 1)
        return None
