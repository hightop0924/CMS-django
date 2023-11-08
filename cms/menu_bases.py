from django.core.exceptions import ValidationError
from django.db.models import Q

from cms.apphook_pool import apphook_pool
from cms.models import Page
from menus.base import Menu


class CMSAttachMenu(Menu):
    cms_enabled = True
    instance = None
    name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                apps.append(app)
        return apps

    @classmethod
    def get_instances(cls):
        """
        Return a list (queryset, really) of all CMS Page objects (in this case)
        that are currently using this CMSAttachMenu either directly as a
        navigation_extender, or, as part of an apphook.

        Calling this DOES perform a DB query.
        """
        parent_apps = []
        for app in cls.get_apphooks():
            parent_apps.append(app.__class__.__name__)
        return Page.objects.filter(
            Q(application_urls__in=parent_apps) | Q(navigation_extenders=cls.__name__)
        )
