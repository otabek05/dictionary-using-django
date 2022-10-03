from unittest.util import _MAX_LENGTH
from django.db import models


class Lugat(models.Model):
    inglizcha=models.CharField('Inglizcha', max_length=120)
    uzbekcha=models.CharField("o'zbekcha", max_length=120)

