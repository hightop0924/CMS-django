from django.forms import MediaDefiningClass

from cms.exceptions import LanguageError
from cms.utils import get_current_site, get_language_from_request
from cms.utils.i18n import get_language_object


class CMSToolbar(metaclass=MediaDefiningClass):
    supported_apps = None

    def __init__(self, request, toolbar, is_current_app, app_path):
        self.request = request
        self.toolbar = toolbar
        self.is_current_app = is_current_app
        self.app_path = app_path
        else:
            local_apps = cls.supported_apps
        for local_app in local_apps:
            if app_name and local_app and app_name.startswith(local_app):
                return True
        return False
