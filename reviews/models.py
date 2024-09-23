from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from songs.models import Song


class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(_("Stars"))
    comment = models.TextField(_("Comment"), null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="reviews")

    def __str__(self) -> str:
        return f"{self.song} | {self.stars}"
