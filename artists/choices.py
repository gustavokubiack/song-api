from django.db import models
from django.utils.translation import gettext_lazy as _

class NationalityTypeChoices(models.TextChoices):
    USA = 'USA', _('Estados Unidos')
    BRAZIL = 'BRAZIL', _('Brasil')
