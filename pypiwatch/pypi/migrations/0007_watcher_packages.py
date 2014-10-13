# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pypi', '0006_package_watchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='watcher',
            name='packages',
            field=models.ManyToManyField(to='pypi.Package', through='pypi.PackageWatchers'),
            preserve_default=True,
        ),
    ]
