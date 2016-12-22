# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibiti_models', '0003_accommodations_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coordinates',
            options={'verbose_name': '\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b', 'verbose_name_plural': '\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': '\u041c\u0435\u0434\u0438\u0430', 'verbose_name_plural': '\u041c\u0435\u0434\u0438\u0430'},
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='bath_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0431\u0430\u043d\u044c'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='bathroom_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0430\u043d\u043d\u044b\u0445'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='bed_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0440\u043e\u0432\u0430\u0442\u0435\u0439'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='bedroom_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043f\u0430\u043b\u0435\u043d'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='check_in_time',
            field=models.TimeField(blank=True, null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0435\u0437\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0413\u043e\u0440\u043e\u0434/\u0420\u0430\u0439\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='comfort_settings',
            field=models.ManyToManyField(blank=True, null=True, to='sibiti_models.ComfortSettings', verbose_name='\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='coords',
            field=models.ManyToManyField(blank=True, null=True, to='sibiti_models.Coordinates', verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='departure_time',
            field=models.TimeField(blank=True, null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u0435\u0437\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0436\u0438\u043b\u044c\u044f'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='guest_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0433\u043e\u0441\u0442\u0435\u0439'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='house_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u043c\u0430'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='inside_toilet_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u0442\u0443\u0430\u043b\u0435\u0442. \u0423\u043d\u0438\u0442\u0430\u0437'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='inside_turkish_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0412\u043d\u0435\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u0442\u0443\u0430\u043b\u0435\u0442. \u0422\u0443\u0440\u0435\u0446\u043a\u0438\u0439'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u0435\u043d'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='placement_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0422\u0438\u043f \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='preview',
            field=models.ManyToManyField(blank=True, null=True, to='sibiti_models.Media', verbose_name='\u0424\u043e\u0442\u043e \u0436\u0438\u043b\u044c\u044f'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0437\u0430 \u0441\u0443\u0442\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='rate',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='shower_in_house_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0443\u0448\u0435\u0432\u044b\u0445 \u0432 \u0434\u043e\u043c\u0435'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='shower_on_street_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0443\u0448\u0435\u0432\u044b\u0445 \u043d\u0430 \u0443\u043b\u0438\u0446\u0435'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0423\u043b\u0438\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0436\u0438\u043b\u044c\u044f'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='traditional_places_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0440\u0430\u0434\u0438\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u043c\u0435\u0441\u0442'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0422\u0438\u043f \u0436\u0438\u043b\u044c\u044f'),
        ),
    ]