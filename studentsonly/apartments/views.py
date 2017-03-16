from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from enrollment.models import People, Profile, Building, Amenities, Apartment, Reviews

def index(request): #List Buildings
    closeList = Building.objects.all().order_by('distanceToCity')
    context = {'closeList':closeList} #creates a dictionary
    return render(request, 'enrollment/index.html', context)
    
#a page for a specific building and list all available apartments
def building(request, building_slug):
    building = Building.objects.get(name_slug=building_slug)
    allApts = Apartment.objects.filter(building__name_slug=building_slug) 
    score = Reviews.objects.filter(building__name_slug=building_slug).#annotate or aggrogate
    
    




