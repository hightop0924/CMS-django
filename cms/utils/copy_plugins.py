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
                # was never updated.
                plugin.save(update_fields=['parent'])
                new_plugins[idx] = plugin.move(parent_plugin, pos="last-child")

    plugins_ziplist = list(zip(new_plugins, old_plugins))

    # this magic is needed for advanced plugins like Text Plugins that can have
    # nested plugins and need to update their content based on the new plugins.
    for new_plugin, old_plugin in plugins_ziplist:
        new_instance = new_plugin.get_plugin_instance()[0]
        if new_instance:
            new_instance._no_reorder = True
            new_instance.post_copy(old_plugin, plugins_ziplist)

    # returns information about originals and copies
    return plugins_ziplist
