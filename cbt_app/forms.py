# coding=utf-8
from django import forms

bedrooms_choices = (
    (1, '1 спальня'),
    (2, '2 спальни'),
    (3, '3 спальни'),
    (4, '4 спальни'),
    (5, '5 спальнен'),
    (6, '6 спальнен'),
    (7, '7 спальнен'),
    (8, '8 спальнен'),
    (9, '9 спальнен'),
    (10, 'Больше 10 спальнен'),
)
bathrooms_choices = (
    (0, '0 ванная'),
    (0.5, '0,5 ванны'),
    (1, '1 ванных'),
)
beds_choices = (
    (1, '1 кровать'),
    (1, '2 кровати'),
    (3, '3 кровати'),
    (4, '4 кровати'),
    (5, '5 кроватей'),
    (6, '6 кроватей'),
    (7, '7 кроватей'),
    (8, 'Больше 8 кроватей'),
)


class AccommodationSearchForm(forms.Form):
    direction = forms.CharField(max_length=255, required=True)
    check_in_date = forms.DateField(required=True)
    check_out_date = forms.DateField(required=True)
    guest_count = forms.IntegerField(required=False)
    accommodation_type = forms.CharField(max_length=255, required=False)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)

    # Size

    bedrooms_count = forms.ChoiceField(choices=bedrooms_choices, required=False)
    bathrooms_count = forms.ChoiceField(choices=bathrooms_choices, required=False)
    beds_count = forms.ChoiceField(choices=beds_choices, required=False)
