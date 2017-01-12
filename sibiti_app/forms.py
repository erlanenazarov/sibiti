# coding=utf-8
from django import forms

bedrooms_choices = (
    (1, '1 спальня'),
    (2, '2 спальни'),
)
bathrooms_choices = (
    (1, '1 ванная'),
    (1.5, '1,5 ванны'),
    (2, '2 ванных'),
)
beds_choices = (
    (1, '1 кровать'),
    (1, '2 кровати'),
    (3, '3 кровати'),
)


class AccommodationSearchForm(forms.Form):
    direction = forms.CharField(max_length=255, required=False)
    check_in_date = forms.DateField(required=False)
    check_out_date = forms.DateField(required=False)
    guest_count = forms.IntegerField(required=False)
    accommodation_type = forms.CharField(max_length=255, required=False)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)

    # Size

    bedrooms_count = forms.ChoiceField(choices=bedrooms_choices, required=False)
    bathrooms_count = forms.ChoiceField(choices=bathrooms_choices, required=False)
    beds_count = forms.ChoiceField(choices=beds_choices, required=False)
