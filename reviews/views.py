from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from reviews.models import Review
from reviews.serializers import ReviewSerializer, ReviewListSerializer
from reviews.filters import ReviewFilter


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReviewFilter

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewListSerializer
        return ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
