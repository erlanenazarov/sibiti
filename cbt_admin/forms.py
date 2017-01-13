from django import forms
from cbt_models.models import *

# Accommodation


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodations
        exclude = ()
        # widgets = {'comfort_settings': forms.CheckboxInput}

    image_1 = forms.ImageField()
    image_2 = forms.ImageField()
    image_3 = forms.ImageField()
    image_4 = forms.ImageField()
    image_5 = forms.ImageField()
    image_6 = forms.ImageField()
    image_7 = forms.ImageField()
    image_8 = forms.ImageField()

