from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from apartments.models import People, Profile, Building, Amenities, Apartment, Reviews

def index(request): #List Apartments
    aptList = Apartment.objects.all()#LATER (order by date-time published)
    context = {'aptList':aptList} #creates a dictionary
    return render(request, 'apartments/index.html', context)
    
def buildingList(request)
    aptList = Apartment.objects.all()
    context =  {'aptList':aptList} 
    return render(request, 'apartments/index.html', context)
    
#a page for a specific building and list all available apartments and all reviews
def building(request, building_slug): #Building detail
    building = Building.objects.get(name_slug=building_slug)
    allReviews = Reviews.objects.filter(building__name_slug=building_slug)
    allApts = Apartment.objects.filter(building__name_slug=building_slug) 
    score = Reviews.objects.filter(building__name_slug=building_slug).aggregate(Avg('rating'))#annotate or aggrogate
    context = {'building':building, 'allReviews':allReviews, 'allApts':allApts, 'score':score}


    




