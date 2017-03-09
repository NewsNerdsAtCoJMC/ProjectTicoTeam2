from django.db import models

class People(models.Model):
    nuid = models.CharField(max_length=8)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    year = models.CharField()
    major = models.CharField()
    
class Building(models.Model):
    name = models.CharField(max_length=255)

class Amenities(models.Model):
    pool = models.BooleanField()

class Apartment(models.Model):
    building = models.ForeignKey(Building)
    amenities = models.ManyToManyField(Amenities)
    description = models.TextField()
    bedrooms = models.IntegerField()
