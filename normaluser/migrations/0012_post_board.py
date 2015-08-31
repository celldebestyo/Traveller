# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normaluser', '0011_auto_20150825_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='board',
            field=models.ForeignKey(blank=True, null=True, to='normaluser.Board'),
        ),
    ]
