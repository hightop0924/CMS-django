from django.conf import settings
from django.urls import re_path

from cms.apphook_pool import apphook_pool
from cms.views import details

if settings.APPEND_SLASH:
    reg = re_path(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', details, name='pages-details-by-slug')
else:
    reg = re_path(r'^(?P<slug>[0-9A-Za-z-_.//]+)$', details, name='pages-details-by-slug')
    from cms.appresolver import get_app_patterns
    urlpatterns = get_app_patterns() + urlpatterns
