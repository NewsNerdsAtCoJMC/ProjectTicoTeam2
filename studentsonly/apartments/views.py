from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from enrollment.models import People, Profile, Building, Amenities, Apartment, Reviews

def index(request):
    closeList = Building.objects.all().order_by('distanceToCity')[:10]
    context = {'closeList':closeList} #creates a dictionary
    return render(request, 'enrollment/index.html', context)

