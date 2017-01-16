from django.shortcuts import render
from django.db.models import Q
from cbt_models.models import *
from forms import *
import datetime


# Create your views here.

def generate_view_params(request):
    params = {
    }
    return params


def index_view(request):
    accommodation = Accommodations.objects.filter(is_active=True).order_by('-id')[:10]
    params = {
        'accommodation': accommodation,
        'accommodation_search_form': AccommodationSearchForm(request.POST)
    }

    return render(request, 'view/index.html', params)


def accommodation_info(request, uid):
    accommodation = Accommodations.objects.get(id=int(uid))

    params = {
        'hotel': accommodation
    }

    return render(request, 'view/accomodation_single.html', params)


def search_accommodations(request):
    filter_form = AccommodationSearchForm(request.POST)
    filter_comforts = ComfortSettings.objects.all()
    params = {
        'filter_form': filter_form,
        'filter_comforts': filter_comforts
    }
    if request.POST:
        if filter_form.is_valid():
            city = filter_form.cleaned_data['direction']
            check_in_date = filter_form.cleaned_data['check_in_date']
            check_out_date = filter_form.cleaned_data['check_out_date']

            prepare_hotels = Accommodations.objects.filter(city=city).exclude(
                reserved_days__date__range=[check_in_date, check_out_date],
                book_days__date__range=[check_in_date, check_out_date]
            )

            params['accommodation'] = prepare_hotels

    return render(request, 'view/accommodation_search_result.html', params)



def apply_filters_to_accommodation_search_results(request):
    if request.is_ajax():
        pass
    pass