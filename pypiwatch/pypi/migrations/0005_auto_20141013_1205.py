# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pypi', '0004_remove_watcher_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='version',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]
