from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, re_path
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve

from cms.utils.conf import get_cms_setting

admin.autodiscover()
    re_path(r'^', include('cms.test_utils.project.third_cms_urls_for_apphook_tests')),
)
