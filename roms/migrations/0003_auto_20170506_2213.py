# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 22:13
from __future__ import unicode_literals

from django.db import migrations
import roms.models
import stdimage.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('roms', '0002_auto_20170506_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rom',
            name='cover',
            field=stdimage.models.StdImageField(upload_to=roms.models.upload_cover_to, verbose_name='cover image'),
        ),
        migrations.AlterField(
            model_name='rom',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
