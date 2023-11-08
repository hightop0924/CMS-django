from django.db.models.base import ModelBase

from cms.publisher.manager import PublisherManager


class PageMetaClass(ModelBase):
    def __new__(cls, name, bases, attrs):
        super_new = super(PageMetaClass, cls).__new__

        if 'objects' in attrs:
