from django.core.management.base import LabelCommand

from cms.models import Page
from cms.models.pluginmodel import CMSPlugin

from .base import SubcommandsCommand


class UninstallApphooksCommand(LabelCommand):
    args = 'APPHOK_NAME'
    command_name = 'apphooks'
    label = 'apphook name (eg SampleApp)'
    help_string = 'Uninstalls (sets to null) specified apphooks for all pages'

    def handle_label(self, label, **options):


class UninstallPluginsCommand(LabelCommand):
    args = 'PLUGIN_NAME'
    command_name = 'plugins'
    label = 'plugin name (eg SamplePlugin)'
    help_string = 'Uninstalls (deletes) specified plugins from the CMSPlugin model'
    missing_args_message = 'foo bar'

    def handle_label(self, label, **options):
        queryset = CMSPlugin.objects.filter(plugin_type=label)
        number_of_plugins = queryset.count()

        if number_of_plugins > 0:
            if options.get('interactive'):
                confirm = input("""
You have requested to remove %d '%s' plugins.
Are you sure you want to do this?
Type 'yes' to continue, or 'no' to cancel: """ % (number_of_plugins, label))
            else:
                confirm = 'yes'
            if confirm == 'yes':
                queryset.delete()
                self.stdout.write("%d '%s' plugins uninstalled\n" % (number_of_plugins, label))
            else:
                self.stdout.write('Aborted')
        else:
            self.stdout.write("no '%s' plugins found\n" % label)


class UninstallCommand(SubcommandsCommand):
    help_string = 'Uninstall objects instances of the following types:'
    command_name = 'uninstall'
    missing_args_message = 'foo bar'
    subcommands = {
        'apphooks': UninstallApphooksCommand,
        'plugins': UninstallPluginsCommand
    }
