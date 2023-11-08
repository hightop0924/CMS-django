from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject


def get_page(request):
    from cms.appresolver import applications_page_check
    from cms.utils.page import get_page_from_request

    if not hasattr(request, '_current_page_cache'):
        request._current_page_cache = get_page_from_request(request)
