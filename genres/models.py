from django.db import models
from django.utils.translation import gettext_lazy as _
from genres.choices import GenreTypeChoices


class Genre(models.Model):
    name = models.CharField(
        _("Name"), max_length=200, choices=GenreTypeChoices.choices, unique=True
    )

    def __str__(self) -> str:
        return self.name
