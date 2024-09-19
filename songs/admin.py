from django.contrib import admin
from songs.models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "genre__name",
        "release_date",
    )
    search_fields = (
        "id",
        "title",
        "genre__name",
    )
