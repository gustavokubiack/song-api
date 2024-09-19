from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class GenreTypeChoices(TextChoices):
    ACTION = "Action", _("Action")
    ADVENTURE = "Adventure", _("Adventure")
    COMEDY = "Comedy", _("Comedy")
    DRAMA = "Drama", _("Drama")
    HORROR = "Horror", _("Horror")
    SCI_FI = "Science Fiction", _("Science Fiction")
    FANTASY = "Fantasy", _("Fantasy")
    ROMANCE = "Romance", _("Romance")
    MYSTERY = "Mystery", _("Mystery")
    THRILLER = "Thriller", _("Thriller")
    ANIMATION = "Animation", _("Animation")
    DOCUMENTARY = "Documentary", _("Documentary")
    MUSICAL = "Musical", _("Musical")
    HISTORICAL = "Historical", _("Historical")
    FAMILY = "Family", _("Family")
