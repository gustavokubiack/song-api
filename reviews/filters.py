import django_filters
from reviews.models import Review


class ReviewFilter(django_filters.FilterSet):
    song__id = django_filters.NumberFilter(field_name="song__id")
    song__title = django_filters.CharFilter(lookup_expr="icontains")
    stars = django_filters.NumberFilter()
    stars__gt = django_filters.NumberFilter(field_name="stars", lookup_expr="gt")
    stars__lt = django_filters.NumberFilter(field_name="stars", lookup_expr="lt")
    user__username = django_filters.CharFilter(field_name="user__username")

    class Meta:
        model = Review
        fields = ["stars", "song", "user"]
