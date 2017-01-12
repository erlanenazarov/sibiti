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
    type = models.CharField(max_length=255, verbose_name='Тип жилья', null=True, blank=True)
    placement_type = models.CharField(max_length=255, verbose_name='Тип размещения', null=True, blank=True)
    guest_count = models.IntegerField(verbose_name='Количество гостей', null=True, blank=True)
    traditional_places_count = models.IntegerField(verbose_name='Количество традиционных мест', null=True, blank=True)
    bedroom_count = models.IntegerField(verbose_name='Количество спален', null=True, blank=True)
    bed_count = models.IntegerField(verbose_name='Количество кроватей', null=True, blank=True)

    # Bathrooms =====================================================================
    bath_count = models.IntegerField(verbose_name='Количество бань', null=True, blank=True)
    shower_in_house_count = models.IntegerField(verbose_name='Количество душевых в доме', null=True, blank=True)
    shower_on_street_count = models.IntegerField(verbose_name='Количество душевых на улице', null=True, blank=True)
    bathroom_count = models.IntegerField(verbose_name='Количество ванных', null=True, blank=True)
    inside_toilet_count = models.IntegerField(verbose_name='Внутренний туалет. Унитаз', null=True, blank=True)
    inside_turkish_count = models.IntegerField(verbose_name='Внетренний туалет. Турецкий', null=True, blank=True)

    # Comfort =======================================================================
    comfort_settings = models.ManyToManyField('ComfortSettings', verbose_name='Удобства', null=True, blank=True)

    # Preview =======================================================================
    preview = models.ManyToManyField('Media', verbose_name='Фото жилья', null=True, blank=True)

    # Location ======================================================================
    region = models.CharField(max_length=255, verbose_name='Регион', null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name='Город/Район', null=True, blank=True)
    street = models.CharField(max_length=255, verbose_name='Улица', null=True, blank=True)
    house_number = models.CharField(max_length=255, verbose_name='Номер дома', null=True, blank=True)
    coords = models.ManyToManyField('Coordinates', verbose_name='Координаты', null=True, blank=True)

    # Price and description =========================================================
    price = models.IntegerField(verbose_name='Цена за сутки', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Наименование жилья', null=True, blank=True)
    description = models.TextField(verbose_name='Описание жилья', null=True, blank=True)

    # Rules and dates ===============================================================
    check_in_time = models.TimeField(verbose_name='Время заезда', null=True, blank=True)
    departure_time = models.TimeField(verbose_name='Время выезда', null=True, blank=True)

    rate = models.FloatField(null=True, default=0.0, blank=True, verbose_name='Рейтинг')

    is_automatic = models.BooleanField(default=False, verbose_name='Мгновенное бронирование')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    has_certificate = models.BooleanField(default=False, verbose_name='Сертификат CBT')
    stars = models.ManyToManyField('Star', verbose_name='Звёзды', null=True, blank=True)

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
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'

    content = models.ImageField(upload_to='', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Описание')

    def __unicode__(self):
        return self.title


class Coordinates(models.Model):
    class Meta:
        db_table = 'coordinates'
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    title = models.CharField(max_length=255, verbose_name='Наименование марки')

    def __unicode__(self):
        return self.title


class Star(models.Model):
    class Meta:
        db_table = 'star'
        verbose_name = 'Звёзда'
        verbose_name_plural = 'Звёзды'

    title = models.CharField(max_length=255, verbose_name='Наименование')
    preview = models.ImageField(upload_to='', verbose_name='Изображение')

    def __unicode__(self):
        return self.title
