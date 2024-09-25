import django_filters
from artists.models import Artist


class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    nationality = django_filters.CharFilter(lookup_expr="icontains")
    birthday = django_filters.NumberFilter(field_name="birthday", lookup_expr="year")
    birthday__gt = django_filters.NumberFilter(
        field_name="birthday", lookup_expr="year__gt"
    )
    birthday__lt = django_filters.NumberFilter(
        field_name="birthday", lookup_expr="year__lt"
    )

    class Meta:
        model = Artist
        fields = ["name", "birthday", "nationality"]
