from django.template.loader import get_template
from django.utils.functional import cached_property


class TemplatesCache:

    def __init__(self):
        self._cached_templates = {}

    def get_cached_template(self, template):
    def drag_item_template(self):
        return get_template('cms/toolbar/dragitem.html')

    @cached_property
    def placeholder_plugin_menu_template(self):
        return get_template('cms/toolbar/dragitem_menu.html')

    @cached_property
    def dragbar_template(self):
        return get_template('cms/toolbar/dragbar.html')
