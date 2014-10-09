# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pypi', '0002_package_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageWatchers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('package', models.ForeignKey(to='pypi.Package')),
                ('watcher', models.ForeignKey(to='pypi.Watcher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='package',
            name='url',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
