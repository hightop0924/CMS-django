from django.db import models

from cms.publisher.query import PublisherQuerySet


class PublisherManager(models.Manager):
    """Manager with some support handling publisher.
    """
    def get_queryset(self):
        """Change standard model queryset to our own.
        """
        return PublisherQuerySet(self.model)

    def drafts(self):
        return self.get_queryset().drafts()
