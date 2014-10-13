# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pypi', '0005_auto_20141013_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='watchers',
            field=models.ManyToManyField(to='pypi.Watcher', through='pypi.PackageWatchers'),
            preserve_default=True,
        ),
    ]
