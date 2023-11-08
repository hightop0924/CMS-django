from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalpagepermission',
            name='sites',
            field=models.ManyToManyField(help_text='If none selected, user haves granted permissions to all sites.', to='sites.Site', verbose_name='sites', blank=True),
