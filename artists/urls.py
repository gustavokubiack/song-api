from django.urls import path
from artists.views import ArtistCreateListView, ArtistRetrieveUpdateDestroyView


urlpatterns = [
    path("artists/", ArtistCreateListView.as_view(), name="artist-create-list"),
    path(
        "artists/<int:pk>/",
        ArtistRetrieveUpdateDestroyView.as_view(),
        name="artist-detail-view",
    ),
]
