# Generated by Django 2.1b1 on 2018-06-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0021_auto_20180507_1432'),
    ]
            name='published',
            field=models.BooleanField(blank=True, default=False, verbose_name='is published'),
        ),
    )