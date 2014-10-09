# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pypi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='version',
            field=models.CharField(default='0.0.0', max_length=25),
            preserve_default=False,
        ),
    ]
