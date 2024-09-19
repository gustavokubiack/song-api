from django.urls import path
from songs.views import SongCreateListView, SongRetrieveUpdateDestroyView


urlpatterns = [
    path("songs/", SongCreateListView.as_view(), name="songs-create-list"),
    path(
        "songs/<int:pk>/",
        SongRetrieveUpdateDestroyView.as_view(),
        name="songs-detail-view",
    ),
]
