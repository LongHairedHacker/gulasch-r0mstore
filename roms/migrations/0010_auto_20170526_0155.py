# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roms', '0009_rom_download_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rom',
            name='download_count',
            field=models.IntegerField(default=0),
        ),
    ]