from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from songs.models import Song
from songs.serializers import SongModelSerializer


class SongCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
