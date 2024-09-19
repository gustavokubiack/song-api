from django.db import models
from songs.models import Song
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(_("Stars"))
    comment = models.TextField(_("Comment"), null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.song} | {self.stars}"
