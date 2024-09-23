from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from songs.models import Song
from songs.serializers import SongModelSerializer, SongDetailSerializer
from songs.filters import SongFilter


class SongCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SongFilter

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SongDetailSerializer
        return SongModelSerializer


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
