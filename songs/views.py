from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from songs.models import Song
from songs.serializers import SongModelSerializer
from songs.filters import SongFilter


class SongCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SongFilter


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
