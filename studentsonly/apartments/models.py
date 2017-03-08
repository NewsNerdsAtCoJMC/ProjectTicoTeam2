from django.db import models

class Building(models.Model):
	name = models.CharField(max_length=255)

class Amenities(models.Model):
	pool = models.BooleanField()
	pets = models.BooleanField()
	cable = models.BooleanField()
	wifi = models.BooleanField()
	electric = models.BooleanField()
	smoking = models.BooleanField()
	electric = models.BooleanField()
	gym = models.BooleanField()
	reservedParking = models.BooleanField()
	coveredParking = models.BooleanField()

class Apartment(models.Model):
	rating = models.ForeignKey(Rating)
	building = models.ForeignKey(Building)
	amenities = models.ManyToManyField(Amenities)
	description = models.TextField()
	distanceToCity = models.BooleanField()
	distanceToEast = models.BooleanField()
	price = models.IntegerField()
	leasingOptions = models.CharField()
	bedrooms = models.IntegerField() #consider changing type

class Rating(models.Model):
	apartment = models.ForeignKey(Apartment)
	text = models.CharField(maxLength=1000)
	hospitality = models.IntegerField() #add validators to restrict max value
	maintenance = models.IntegerField()
	safety_security = models.IntegerField()