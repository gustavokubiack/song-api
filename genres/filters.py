import django_filters
from genres.models import Genre


class GenreFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Genre
        fields = ["name"]
