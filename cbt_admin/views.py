# coding=utf-8
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
from cbt_main import settings

from cbt_models.models import *
from forms import *


# Create your views here.


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN,
                        secure=settings.SESSION_COOKIE_SECURE or None)
    return response


# Accommodation constructor

def constructor(request):
    form = AccommodationForm
    comfort_settings = ComfortSettings.objects.all()

    params = {
        'accommodation_form': form,
        'comfort_settings': comfort_settings
    }

    return render(request, 'view/user/add_accommodation/constructor.html', params)



