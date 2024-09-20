from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from artists.models import Artist
from artists.serializers import ArtistModelSerializer
from artists.filters import ArtistFilter


class ArtistCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArtistFilter


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer
