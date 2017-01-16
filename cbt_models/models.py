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
    type = models.ForeignKey('AccommodationType', verbose_name=u'Тип жилья', null=True, blank=True)
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
    outside_toilet_count = models.IntegerField(verbose_name='Внешний туалет.', null=True, blank=True)

    # Comfort =======================================================================
    comfort_settings = models.ManyToManyField('ComfortSettings', verbose_name='Удобства', null=True, blank=True)
    # wi_fi_internet = models.BooleanField(default=False, verbose_name='Wi-Fi')
    # tv = models.BooleanField(default=False, verbose_name='Телевизор')
    # kitchen = models.BooleanField(default=False, verbose_name='Кухня')
    # breakfast = models.BooleanField(default=False, verbose_name='Завтрак')
    # bedroom_secure = models.BooleanField(default=False, verbose_name='Замок в спальню')
    # internet = models.BooleanField(default=False, verbose_name='Интернет')
    # kab_tv = models.BooleanField(default=False, verbose_name='Кабельное телевиденье')
    # fireplace = models.BooleanField(default=False, verbose_name='Камин')
    # air_condition = models.BooleanField(default=False, verbose_name='Кондиционер')
    # working_place = models.BooleanField(default=False, verbose_name='Место для работы на ноутбуке')
    # heating = models.BooleanField(default=False, verbose_name='Отопление')
    # hanger = models.BooleanField(default=False, verbose_name='Плечики')
    # family_children_available = models.BooleanField(default=False, verbose_name='Подходит для детей/семьи')
    # check_in_time_fully = models.BooleanField(default=False, verbose_name='Прибытие кругло суточно')

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

    reserved_days = models.ManyToManyField('DateHelper', verbose_name='Зарезервированные дни', related_name='reserved_days', null=True, blank=True)

    book_days = models.ManyToManyField('DateHelper', verbose_name='Забронированные дни', related_name='book_days', null=True, blank=True)

    def __unicode__(self):
        return str(self.id)


class ComfortSettings(models.Model):
    class Meta:
        verbose_name = 'Удобства'
        verbose_name_plural = 'Удобства'

    title = models.CharField(max_length=255, verbose_name='Наименования')

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


class DateHelper(models.Model):
    class Meta:
        db_table = 'date_helper'
        verbose_name = 'Дату'
        verbose_name_plural = 'Даты'

    date = models.DateField(verbose_name='Дата')

    def __unicode__(self):
        return str(self.date)


class AccommodationType(models.Model):
    class Meta:
        db_table = 'accommodation_type'
        verbose_name = 'Тип жилья'
        verbose_name_plural = 'Типы жилья'

    title = models.CharField(max_length=255, verbose_name='Наименование')

    def __unicode__(self):
        return self.title
