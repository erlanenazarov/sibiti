# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibiti_models', '0004_auto_20161222_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodations',
            name='has_certificate',
            field=models.BooleanField(default=False, verbose_name='\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442 CBT'),
        ),
    ]
