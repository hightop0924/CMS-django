from django.conf import settings

from cms.plugin_base import CMSPluginBase, PluginMenuItem
from cms.plugin_pool import plugin_pool


class EmptyPlugin(CMSPluginBase):
    name = "Empty Plugin"
    text_enabled = True
    render_plugin = False

    def render(self, context, instance, placeholder):
        return context

    def icon_src(self, instance):
