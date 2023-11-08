import uuid

from django.db import models


class UrlconfRevision(models.Model):
    revision = models.CharField(max_length=255)

    class Meta:
        app_label = 'cms'
        Convenience method for getting or creating revision.
        """
        if revision is None:
            revision = str(uuid.uuid4())
        obj, created = cls.objects.get_or_create(
            pk=1, defaults={"revision": revision})
        return obj.revision, created

    @classmethod
    def update_revision(cls, revision):
        """
        Convenience method for updating the revision.
        """
        obj, created = cls.objects.get_or_create(
            pk=1, defaults={"revision": revision})
        if not created:
            obj.revision = revision
            obj.save()
