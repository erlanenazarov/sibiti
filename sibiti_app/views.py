from django.shortcuts import render
from sibiti_models.models import *

# Create your views here.


def register_accommodations(request):
    accommodation = Accommodations.objects.all().order_by('-id')[:10]
    usd_currency = 69.2
    hotels = list()

    for hotel in accommodation:
        price_usd = round(hotel.price / usd_currency, 2)
        item = dict(
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
        'accommodation': hotels
    }

    return render(request, 'view/index.html', params)
