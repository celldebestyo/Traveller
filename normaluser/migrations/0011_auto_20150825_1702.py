# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normaluser', '0010_board_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='followers',
            field=models.ManyToManyField(related_name='board_followers', blank=True, null=True, to='normaluser.NormalUser'),
        ),
        migrations.AlterField(
            model_name='board',
            name='participants',
            field=models.ManyToManyField(related_name='participants', blank=True, null=True, to='normaluser.NormalUser'),
        ),
    ]
