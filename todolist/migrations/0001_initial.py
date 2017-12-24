# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('begin', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('end', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.IntegerField(default=1, choices=[(0, b'Urgent'), (1, b'Normal')])),
                ('finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
