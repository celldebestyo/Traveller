# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normaluser', '0003_auto_20150809_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='gender',
            field=models.CharField(default='Male', max_length=10),
        ),
    ]
