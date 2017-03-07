from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=255)

class Amenities(models.Model):
	
class Apartment(models.Model):
    building = models.ForeignKey(Building)
    amenities = models.ManyToManyField(Amenities)
    description = models.TextField()
    bedrooms = models.IntegerField()
