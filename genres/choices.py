from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class GenreTypeChoices(TextChoices):
    POP = "Pop", _("Pop")
    ROCK = "Rock", _("Rock")
    JAZZ = "Jazz", _("Jazz")
    HIP_HOP = "Hip Hop", _("Hip Hop")
    CLASSICAL = "Classical", _("Classical")
    COUNTRY = "Country", _("Country")
    REGGAE = "Reggae", _("Reggae")
    BLUES = "Blues", _("Blues")
    ELECTRONIC = "Electronic", _("Electronic")
    METAL = "Metal", _("Metal")
    FOLK = "Folk", _("Folk")
    R_AND_B = "R&B", _("R&B")
    LATIN = "Latin", _("Latin")
    SOUL = "Soul", _("Soul")
