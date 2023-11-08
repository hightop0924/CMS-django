from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import MultiColumnForm
from .models import MultiColumns


class MultiColumnPlugin(CMSPluginBase):
    model = MultiColumns
        for _x in range(int(form.cleaned_data['create'])):
            col = CMSPlugin(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=CMSPlugin.objects.filter(parent=obj).count(),
                plugin_type=ColumnPlugin.__name__
            )
            col.save()
        return response


class ColumnPlugin(CMSPluginBase):
    module = "Multi Columns"
    name = "Column"
    render_template = 'pluginapp/multicolumn/column.html'
    parent_classes = ["MultiColumnPlugin"]
    allow_children = True


plugin_pool.register_plugin(MultiColumnPlugin)
plugin_pool.register_plugin(ColumnPlugin)
