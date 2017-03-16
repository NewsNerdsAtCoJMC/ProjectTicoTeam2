from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from enrollment.models import People, Profile, Building, Amenities, Apartment, Reviews

def index(request): #List Buildings
    closeList = Building.objects.all().order_by('distanceToCity')[:10]
    context = {'closeList':closeList} #creates a dictionary
    return render(request, 'enrollment/index.html', context)
    
#a page for a specific building
def building(request, building_slug):
    building = Building.objects.get(name=building_slug)
    
    
#list apartments in a given building
def apartments(request, 





