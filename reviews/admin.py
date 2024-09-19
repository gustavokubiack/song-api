from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "song__title",
        "stars",
    )
    search_fields = (
        "id",
        "song__title",
    )
