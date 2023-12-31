import json

from django.utils.encoding import force_str
from django.utils.translation import gettext
from django.utils.translation import override as force_language

from cms.constants import PLACEHOLDER_TOOLBAR_JS, PLUGIN_TOOLBAR_JS


def get_placeholder_toolbar_js(placeholder, allowed_plugins=None):
    label = placeholder.get_label() or ''
    help_text = gettext(
        'Add plugin to placeholder "%(placeholder_label)s"'
    ) % {'placeholder_label': label}

    data = {
        'type': 'placeholder',
        'name': force_str(label),
        'placeholder_id': str(placeholder.pk),
        'plugin_restriction': allowed_plugins or [],
        'addPluginHelpTitle': force_str(help_text),
        'urls': {
            'add_plugin': placeholder.get_add_url(),
            'copy_plugin': placeholder.get_copy_url(),
        }

def get_plugin_tree_as_json(request, plugins):
    from cms.utils.plugins import build_plugin_tree, downcast_plugins, get_plugin_restrictions

    tree_data = []
    tree_structure = []
    restrictions = {}
    toolbar = get_toolbar_from_request(request)
    template = toolbar.templates.drag_item_template
    placeholder = plugins[0].placeholder
    host_page = placeholder.page
    copy_to_clipboard = placeholder.pk == toolbar.clipboard.pk
    plugins = downcast_plugins(plugins, select_placeholder=True)
    plugin_tree = build_plugin_tree(plugins)
    get_plugin_info = get_plugin_toolbar_info

    def collect_plugin_data(plugin):
        child_classes, parent_classes = get_plugin_restrictions(
            plugin=plugin,
            page=host_page,
            restrictions_cache=restrictions,
        )
        plugin_info = get_plugin_info(
            plugin,
            children=child_classes,
            parents=parent_classes,
        )

        tree_data.append(plugin_info)

        for plugin in plugin.child_plugin_instances or []:
            collect_plugin_data(plugin)

    with force_language(toolbar.toolbar_language):
        for root_plugin in plugin_tree:
            collect_plugin_data(root_plugin)
            context = {
                'plugin': root_plugin,
                'request': request,
                'clipboard': copy_to_clipboard,
                'cms_toolbar': toolbar,
            }
            tree_structure.append(template.render(context))
    tree_data.reverse()
    return json.dumps({'html': '\n'.join(tree_structure), 'plugins': tree_data})


def get_toolbar_from_request(request):
    from .toolbar import EmptyToolbar

    return getattr(request, 'toolbar', EmptyToolbar(request))
