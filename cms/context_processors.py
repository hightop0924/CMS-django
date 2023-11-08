from functools import lru_cache

from django.utils.functional import lazy

from cms.utils.conf import get_cms_setting
from cms.utils.page import get_page_template_from_request


def cms_settings(request):
    """
    # Now use lazy() to avoid getting the menu renderer
    # up until the point is needed.
    # lazy() does not memoize results, is why lru_cache is needed.
    _get_menu_renderer = lazy(_get_menu_renderer, MenuRenderer)

    return {
        'cms_menu_renderer': _get_menu_renderer(),
        'CMS_MEDIA_URL': get_cms_setting('MEDIA_URL'),
        'CMS_TEMPLATE': lambda: get_page_template_from_request(request),
    }
