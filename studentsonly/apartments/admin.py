from django.contrib import admin

from .models import Profile, Building, Amenities, Apartment, Reviews

admin.site.register(Profile)
admin.site.register(Building)
admin.site.register(Amenities)
admin.site.register(Apartment)
admin.site.register(Reviews)