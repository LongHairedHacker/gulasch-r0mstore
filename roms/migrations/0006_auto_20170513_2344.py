# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roms', '0005_rom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rom',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='approved'),
        ),
        migrations.AlterField(
            model_name='rom',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]