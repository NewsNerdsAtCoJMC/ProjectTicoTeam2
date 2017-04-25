from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Avg
from apartments.models import Profile, Building, Amenities, Apartment, Reviews
from apartments.forms import ApartmentForm

def index(request): #List Apartments
    aptList = Apartment.objects.all()#LATER (order by date-time published)
    context = {'aptList':aptList} #creates a dictionary
    return render(request, 'apartments/index.html', context)
    
def buildingList(request):
    buildingList = Building.objects.all()
    context = {'aptList':aptList} 
    return render(request, 'template here', context)
    
#a page for a specific building and list all available apartments and all reviews
def building(request, building_slug): #Building detail
    building = Building.objects.get(name_slug=building_slug)
    allReviews = Reviews.objects.filter(building__name_slug=building_slug)
    allApts = Apartment.objects.filter(building__name_slug=building_slug) 
    score = Reviews.objects.filter(building__name_slug=building_slug).aggregate(Avg('overall'))#annotate or aggrogate
    context = {'building':building, 'allReviews':allReviews, 'allApts':allApts, 'score':score}
    return render(request, 'apartments/building.html', context)

def apartmentDetail(request, listing_id):
    listing = Apartment.objects.get(id=listing_id)
    context = {'listing': listing}
    return render(request, 'apartments/detail.html', context)
    
def postlisting(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('/')
    else:
        form = ApartmentForm()
        context = {'form': form}
    return render(request, 'apartments/post.html', context)
    
def postreview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('/')
    else:
        form = ReviewForm()
        context = {'form': form}
    return render(request, 'apartments/post.html', context)
    
    





