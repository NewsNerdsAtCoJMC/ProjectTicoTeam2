from django.contrib import admin

from .models import Profile, Building, Amenities, Apartment, People, Reviews

admin.site.register(Profile)
admin.site.register(Building)
admin.site.register(Amenities)
admin.site.register(Apartment)
admin.site.register(People)
admin.site.register(Reviews)