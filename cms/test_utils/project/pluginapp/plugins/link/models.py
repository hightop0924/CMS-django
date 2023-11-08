from django.db import models

from cms.models import CMSPlugin


class Link(CMSPlugin):
    name = models.CharField(
        verbose_name='Display name',
        max_length=255,
    )
    external_link = models.URLField(
        verbose_name='External link',
        max_length=2040,
    )

