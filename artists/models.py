from django.db import models
from django.utils.translation import gettext_lazy as _


class Artist(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    birthday = models.DateField(_("Birthday"), null=True, blank=True)
    nationality = models.CharField(
        _("Nationality"),
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
