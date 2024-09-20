import django_filters
from songs.models import Song


class SongFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    genre__name = django_filters.CharFilter(lookup_expr="icontains")
    genre__id = django_filters.NumberFilter(field_name="genre__id")
    release_date = django_filters.NumberFilter(
        field_name="release_date", lookup_expr="year"
    )
    release_date__gt = django_filters.NumberFilter(
        field_name="release_date", lookup_expr="year__gt"
    )
    release_date__lt = django_filters.NumberFilter(
        field_name="release_date", lookup_expr="year__lt"
    )
    artists__id = django_filters.NumberFilter(field_name="artists__id")
    artists__name = django_filters.CharFilter(
        field_name="artists__name", lookup_expr="icontains"
    )

    class Meta:
        model = Song
        fields = ["title", "genre", "release_date", "artists"]
