# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('calendar', models.ForeignKey(to='normaluser.Calendar')),
            ],
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', blank=True, null=True)),
                ('location', models.CharField(max_length=255, blank=True, null=True)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('phoneNumber', models.CharField(max_length=30, blank=True, null=True)),
                ('postalCode', models.CharField(max_length=30, blank=True, null=True)),
                ('IdentityNumber', models.CharField(max_length=30, blank=True, null=True)),
                ('followers', models.ManyToManyField(related_name='followerfwqfwqs', to='normaluser.NormalUser', blank=True)),
                ('followings', models.ManyToManyField(related_name='following', to='normaluser.NormalUser', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', blank=True, null=True)),
                ('description', models.TextField()),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('likeCount', models.IntegerField(default=0)),
                ('sharedCount', models.IntegerField(default=0)),
                ('relatedAs', models.CharField(max_length=255)),
                ('author', models.ForeignKey(to='normaluser.NormalUser', related_name='author')),
                ('owner', models.ForeignKey(to='normaluser.NormalUser', related_name='owner')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='invitees',
            field=models.ManyToManyField(to='normaluser.NormalUser'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='user',
            field=models.ForeignKey(to='normaluser.NormalUser'),
        ),
        migrations.AddField(
            model_name='board',
            name='admin',
            field=models.ForeignKey(to='normaluser.NormalUser', related_name='admin'),
        ),
        migrations.AddField(
            model_name='board',
            name='followers',
            field=models.ManyToManyField(related_name='board_followers', to='normaluser.NormalUser'),
        ),
        migrations.AddField(
            model_name='board',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to='normaluser.NormalUser'),
        ),
    ]
