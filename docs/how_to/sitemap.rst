######################
How to create sitemaps
######################


*******
Sitemap
*******

Sitemaps are XML files used by Google to index your website by using their
   setting
 * add ``from cms.sitemaps import CMSSitemap`` to the top of your main ``urls.py``
 * add ``from django.contrib.sitemaps.views import sitemap`` to ``urls.py```
 * add ``url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),``
   to your ``urlpatterns``


***************************
``django.contrib.sitemaps``
***************************

More information about :mod:`django.contrib.sitemaps` can be found in the official
`Django documentation <http://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/>`_.


