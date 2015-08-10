# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('normaluser', '0002_auto_20150804_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='birthDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
