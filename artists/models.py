from django.db import models
from django.utils.translation import gettext_lazy as _
from artists.choices import NationalityTypeChoices


class Artist(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    birthday = models.DateField(_("Birthday"), null=True, blank=True)
    nacionality = models.CharField(
        _("Nationality"),
        max_length=100,
        choices=NationalityTypeChoices.choices,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
