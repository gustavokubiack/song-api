from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from artists.models import Artist
from artists.serializers import ArtistModelSerializer


class ArtistCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer
