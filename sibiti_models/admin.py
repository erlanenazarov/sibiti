from django.contrib import admin
from models import *

# Register your models here.


class AccommodationAdmin(admin.ModelAdmin):
    list_display = 'title price type guest_count'.split()
    list_filter = 'price type guest_count'.split()


admin.site.register(Accommodations, AccommodationAdmin)
admin.site.register(ComfortSettings)
admin.site.register(Media)
admin.site.register(Coordinates)
admin.site.register(Star)
