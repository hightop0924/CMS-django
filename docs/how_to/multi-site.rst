#######################
Multi-Site Installation
#######################

For operating multiple websites using the same virtualenv you can use copies of ``manage.py``,
``wsgi.py`` and different versions of settings and the URL configuration for each site. You can
use the same database for different websites or, if you want a stricter separation, different
databases. You can define settings for all sites in a file that is imported in the site-specific
settings, e. g. ``my_project/base_settings.py``. At the end of these site-specific settings you can
import local settings, which are not under version control, with SECRET_KEY, DATABASES,
ALLOWED_HOSTS etc., which may be site-specific or not.

#.  Copy and edit ``wsgi.py`` and ``manage.py``  e. g. to ``wsgi_second_site.py`` and
    ``manage_second_site.py``: Change the reference to the settings like
    ``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings_second_site")``, if the

        from .settings_local import *

#.  In the web server settings for a site you refer to the site-specific ``wsgi*.py`` like
    ``wsgi_second_site.py``.

