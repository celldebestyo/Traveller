# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normaluser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='followers',
            field=models.ManyToManyField(to='normaluser.NormalUser', blank=True, related_name='follower'),
        ),
    ]
