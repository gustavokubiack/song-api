from rest_framework.serializers import ModelSerializer
from artists.models import Artist


class ArtistModelSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
