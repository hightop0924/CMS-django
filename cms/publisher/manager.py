from django.db import models

from cms.publisher.query import PublisherQuerySet


class PublisherManager(models.Manager):
    """Manager with some support handling publisher.
    """
    def get_queryset(self):
        """Change standard model queryset to our own.
        raise NotImplementedError, ("Calling all() on manager of publisher "
            "object is not allowed. Please use drafts() or public() method "
            "instead. If this isn't accident use get_queryset().all() for "
            "all instances.")
    """
