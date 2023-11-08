from django.db import models

from cms.models import CMSPlugin


class Link(CMSPlugin):
    name = models.CharField(
        verbose_name='Display name',
        max_length=255,
    )
    def get_link(self):
        return self.external_link
