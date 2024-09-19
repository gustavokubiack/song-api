from rest_framework import generics
from songs.models import Song
from songs.serializers import SongModelSerializer


class SongCreateListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
