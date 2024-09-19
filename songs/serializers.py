from rest_framework.serializers import ModelSerializer
from songs.models import Song


class SongModelSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
