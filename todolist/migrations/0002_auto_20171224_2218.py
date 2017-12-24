# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.CharField(default=b'NORMAL', max_length=6, choices=[(b'URGENT', b'Urgent'), (b'NORMAL', b'Normal')]),
        ),
    ]
