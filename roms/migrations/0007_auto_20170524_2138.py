# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import roms.models
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    dependencies = [
        ('roms', '0006_auto_20170513_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rom',
            name='cover',
            field=stdimage.models.StdImageField(upload_to=roms.models.upload_cover_to, validators=[stdimage.validators.MinSizeValidator(300, 300)], verbose_name='cover-Bild'),
        ),
        migrations.AlterField(
            model_name='rom',
            name='description',
            field=models.TextField(verbose_name='Beschreibung'),
        ),
    ]