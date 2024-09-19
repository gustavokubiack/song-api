from django.db.models import Avg
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from songs.models import Song
from reviews.models import Review


class SongModelSerializer(ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = "__all__"

    def get_rate(self, obj: Song) -> float | None:
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return round(rate, 1)
        return None
