
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, re_path
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve

from cms.test_utils.project.placeholderapp.views import example_view

urlpatterns += staticfiles_urlpatterns()


urlpatterns += i18n_patterns(
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^example/$', example_view),
    re_path(r'^', include('cms.urls')),
)
