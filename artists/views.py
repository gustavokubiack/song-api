from rest_framework import generics
from artists.models import Artist
from artists.serializers import ArtistModelSerializer


class ArtistCreateListView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer
