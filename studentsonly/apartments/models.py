from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    noise = models.PositiveIntegerField() #5: ok with loud music, 1: need silence
    social_academic = models.PositiveIntegerField()#5: ok with loud music, 1: need silence
    temp = models.PositiveIntegerField()#5 warm, 1: cool
    cleanliness = models.PositiveIntegerField()#5 very clean 1 total mess
    visitors = models.PositiveIntegerField()#5 like them 1 hate them
    drinking = models.PositiveIntegerField()# 5 i drink a lot - 1: never drink
    smoking = models.CharField(max_length=255)#todo:restrict options #yes. #no, but okay. #no, not okay.
    sleepTime = models.CharField(max_length=255)#todo:restrict options #early riser #night owl
    durationOfStayMonths = models.PositiveIntegerField()
    interests = models.CharField(max_length=1000)

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
    
class Building(models.Model):
    image = models.ImageField(upload_to="media", blank=True, null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contactInfo = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0) #derived from reviews
    #hospitality = models.FloatField(default=0.0) #derived from reviews
    #maintenance = models.FloatField(default=0.0) #derived from reviews
    #safety_security = models.FloatField(default=0.0) #derived from reviews
    amenities = models.ManyToManyField(Amenities)
    distanceToCity = models.FloatField()
    distanceToEast = models.FloatField()
    available = models.BooleanField()
    name_slug = models.SlugField(default="building-name")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/building/%s" % self.name_slug

class Apartment(models.Model):
    nickname = models.CharField(max_length=255)
    building = models.ForeignKey(Building)
    description = models.TextField()
    price = models.IntegerField()
    leasingOptions = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField()
    public = models.BooleanField(default=False)
    def __str__(self):
        return self.nickname
    def get_absolute_url(self):
        return "/apartments/listing/%s" % self.id
    
class Reviews(models.Model):
    name = models.CharField(max_length=255)
    building = models.ForeignKey(Building)
    comment = models.TextField()
    hospitality = models.PositiveIntegerField() 
    maintenance = models.PositiveIntegerField()
    safety_security = models.PositiveIntegerField()
    overall = models.PositiveIntegerField()
    def __str__(self):
        return "%s" % self.overall