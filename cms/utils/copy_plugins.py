def copy_plugins_to(old_plugins, to_placeholder,
                    to_language=None, parent_plugin_id=None, no_signals=False):
    """
    Copies a list of plugins to a placeholder to a language.
    """
    # TODO: Refactor this and copy_plugins to cleanly separate plugin tree/node
    # copying and remove the need for the mutating parameter old_parent_cache.
    old_parent_cache = {}
    # For subplugin copy, top-level plugin's parent must be nulled
    # before copying.
    if old_plugins:
        old_parent = old_plugins[0].parent
        for old_plugin in old_plugins:
            if old_plugin.parent == old_parent:
                old_plugin.parent = old_plugin.parent_id = None
    new_plugins = []
    for old in old_plugins:
        new_plugins.append(
            old.copy_plugin(to_placeholder, to_language or old.language,
                            old_parent_cache, no_signals))

    if new_plugins and parent_plugin_id:
        from cms.models import CMSPlugin
        parent_plugin = CMSPlugin.objects.get(pk=parent_plugin_id)
        for idx, plugin in enumerate(new_plugins):
