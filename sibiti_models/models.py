# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# Accommodations =============================
class Accommodations(models.Model):
    class Meta:
        db_table = 'accommodations'
        verbose_name = 'Жильё'
        verbose_name_plural = 'Жилища'

    # Main Information =============================================================
    type = models.CharField(max_length=255, verbose_name='Тип жилья')
    placement_type = models.CharField(max_length=255, verbose_name='Тип размещения')
    guest_count = models.IntegerField(verbose_name='Количество гостей')
    traditional_places_count = models.IntegerField(verbose_name='Количество традиционных мест')
    bedroom_count = models.IntegerField(verbose_name='Количество спален')
    bed_count = models.IntegerField(verbose_name='Количество кроватей')

    # Bathrooms =====================================================================
    bath_count = models.IntegerField(verbose_name='Количество бань')
    shower_in_house_count = models.IntegerField(verbose_name='Количество душевых в доме')
    shower_on_street_count = models.IntegerField(verbose_name='Количество душевых на улице')
    bathroom_count = models.IntegerField(verbose_name='Количество ванных')
    inside_toilet_count = models.IntegerField(verbose_name='Внутренний туалет. Унитаз')
    inside_turkish_count = models.IntegerField(verbose_name='Внетренний туалет. Турецкий')

    # Comfort =======================================================================
    comfort_settings = models.ManyToManyField('ComfortSettings', verbose_name='Удобства')

    # Preview =======================================================================
    preview = models.ManyToManyField('Media', verbose_name='Фото жилья')

    # Location ======================================================================
    region = models.CharField(max_length=255, verbose_name='Регион')
    city = models.CharField(max_length=255, verbose_name='Город/Район')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=255, verbose_name='Номер дома')
    coords = models.ManyToManyField('Coordinates', verbose_name='Координаты')

    # Price and description =========================================================
    price = models.IntegerField(verbose_name='Цена за сутки')
    title = models.CharField(max_length=255, verbose_name='Наименование жилья')
    description = models.TextField(verbose_name='Описание жилья')

    # Rules and dates ===============================================================
    check_in_time = models.TimeField(verbose_name='Время заезда')
    departure_time = models.TimeField(verbose_name='Время выезда')

    rate = models.FloatField(null=True, default=0.0, blank=True)

    def __unicode__(self):
        return str(self.id)


class ComfortSettings(models.Model):
    class Meta:
        verbose_name = 'Удобства'
        verbose_name_plural = 'Удобства'

    title = models.CharField(max_length=255, verbose_name='Наименования')
    value = models.BooleanField(verbose_name='Значение')

    def __unicode__(self):
        return self.title


class Media(models.Model):
    class Meta:
        db_table = 'media'

    content = models.ImageField(upload_to='', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Описание')

    def __unicode__(self):
        return self.title


class Coordinates(models.Model):
    class Meta:
        db_table = 'coordinates'

    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    title = models.CharField(max_length=255, verbose_name='Наименование марки')

    def __unicode__(self):
        return self.title
