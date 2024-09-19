from django.db.models import Avg
from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def validate_stars(self, stars):
        if stars > 5:
            raise serializers.ValidationError("Rating cannot be greater than 5")
        if stars < 0:
            raise serializers.ValidationError("Rating cannot be less than 0")
        return stars
