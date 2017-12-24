# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20171224_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='finished',
            field=models.CharField(default=b'INCOMPLETE', max_length=10, choices=[(b'COMPLETE', b'Complete'), (b'INCOMPLETE', b'Incomplete')]),
        ),
    ]
