from django.shortcuts import render
from cbt_models.models import *
from forms import *


# Create your views here.

def generate_view_params(request):
    params = {
    }
    return params


def index_view(request):
    accommodation = Accommodations.objects.filter(is_active=True).order_by('-id')[:10]
    usd_currency = 69.2
    hotels = list()

    for hotel in accommodation:
        price_usd = round(hotel.price / usd_currency, 2)
        item = dict(
            id=hotel.id,
            type=hotel.type,
            placement_type=hotel.placement_type,
            guest_count=hotel.guest_count,
            traditional_places_count=hotel.traditional_places_count,
            bedroom_count=hotel.bedroom_count,
            bed_count=hotel.bed_count,
            bath_count=hotel.bath_count,
            shower_in_house_count=hotel.shower_in_house_count,
            shower_on_street_count=hotel.shower_on_street_count,
            bathroom_count=hotel.bathroom_count,
            inside_toilet_count=hotel.inside_toilet_count,
            inside_turkish_count=hotel.inside_turkish_count,
            comfort_settings=hotel.comfort_settings,
            preview=hotel.preview,
            region=hotel.region,
            city=hotel.city,
            street=hotel.street,
            house_number=hotel.house_number,
            coords=hotel.coords,
            price=hotel.price,
            price_usd=price_usd,
            title=hotel.title,
            description=hotel.description,
            check_in_time=hotel.check_in_time,
            departure_time=hotel.departure_time,
            rate=hotel.rate
        )
        hotels.append(item)

    params = {
        'accommodation': hotels,
        'accommodation_search_form': AccommodationSearchForm
    }

    return render(request, 'view/index.html', params)


def accommodation_info(request, uid):
    accommodation = Accommodations.objects.get(id=int(uid))
    usd_currency = 69.2
    price_usd = round(accommodation.price / usd_currency, 2)

    item = dict(
        id=accommodation.id,
        type=accommodation.type,
        placement_type=accommodation.placement_type,
        guest_count=accommodation.guest_count,
        traditional_places_count=accommodation.traditional_places_count,
        bedroom_count=accommodation.bedroom_count,
        bed_count=accommodation.bed_count,
        bath_count=accommodation.bath_count,
        shower_in_house_count=accommodation.shower_in_house_count,
        shower_on_street_count=accommodation.shower_on_street_count,
        bathroom_count=accommodation.bathroom_count,
        inside_toilet_count=accommodation.inside_toilet_count,
        inside_turkish_count=accommodation.inside_turkish_count,
        comfort_settings=accommodation.comfort_settings,
        preview=accommodation.preview,
        region=accommodation.region,
        city=accommodation.city,
        street=accommodation.street,
        house_number=accommodation.house_number,
        coords=accommodation.coords,
        price=accommodation.price,
        price_usd=price_usd,
        title=accommodation.title,
        description=accommodation.description,
        check_in_time=accommodation.check_in_time,
        departure_time=accommodation.departure_time,
        rate=accommodation.rate
    )

    params = {
        'hotel': item
    }

    return render(request, 'view/accomodation_single.html', params)


def search_accommodations(request):
    filter_form = AccommodationSearchForm(request.POST)
    params = {
        'filter_form': filter_form
    }
    if request.POST:

        pass
    return render(request, 'view/accommodation_search_result.html', params)

