# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-17 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0005_auto_20200216_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='live_site',
            field=models.URLField(max_length=300),
        ),
    ]