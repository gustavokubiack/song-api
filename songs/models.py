from django.db import models
from django.utils.translation import gettext_lazy as _
from artists.models import Artist
from genres.models import Genre


class Song(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    release_date = models.DateField(_("Release Date"), null=True, blank=True)
    artists = models.ManyToManyField(Artist, related_name="songs")
    resume = models.TextField(_("Resume"), null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.genre.name}"
