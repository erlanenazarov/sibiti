# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibiti_models', '0002_accommodations_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodations',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
