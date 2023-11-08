from django.db import models

from cms.models.fields import PlaceholderField


class MainModel(models.Model):
    pass

class Translations(models.Model):
    master = models.ForeignKey(MainModel, on_delete=models.CASCADE)
