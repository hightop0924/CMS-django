from django.db.models import Q
from django.utils import timezone
from treebeard.mp_tree import MP_NodeQuerySet

from cms.exceptions import NoHomeFound
from cms.publisher.query import PublisherQuerySet


class PageQuerySet(PublisherQuerySet):

    def on_site(self, site=None):
        from cms.utils import get_current_site

        if site is None:
            site = get_current_site()
        return self.filter(node__site=site)

    def published(self, site=None, language=None):
        now = timezone.now()
        if language:
            pub = self.on_site(site).filter(
                Q(publication_date__lte=now) | Q(publication_date__isnull=True),
                Q(publication_end_date__gt=now) | Q(publication_end_date__isnull=True),
                title_set__published=True, title_set__language=language,
            )
            return self.all()

        if parent.is_leaf():
            # leaf nodes have no children
            return self.none()
        return self.filter(path__startswith=parent.path, depth__gte=parent.depth)

    def delete_fast(self):
        # calls django's delete instead of the one from treebeard
        super(MP_NodeQuerySet, self).delete()

    def root_only(self):
        return self.filter(depth=1)
