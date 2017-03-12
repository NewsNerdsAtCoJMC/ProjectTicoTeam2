from django.db import models

class People(models.Model):
	email = models.CharField(max_length=255)
	reviews = models.ManyToManyField(Reviews)
	apartmentPreferences = models.ForeignKey(Apartment) #search
	profile = models.ForeignKey(Profile)
	phone = models.CharField(max_length=20)
	birthday = models.DateField()
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	year = models.CharField(max_length=255)
	major = models.CharField(max_length=255)

class Profile(models.Model):
	noise = models.PositiveIntegerField() #5: ok with loud music, 1: need silence
	social_academic = models.PositiveIntegerField()#5: ok with loud music, 1: need silence
	temp = models.PositiveIntegerField()#5 warm, 1: cool
	cleanliness = models.PositiveIntegerField()#5 very clean 1 total mess
	visitors = models.PositiveIntegerField()#5 like them 1 hate them
	drinking = models.PositiveIntegerField()# 5 i drink a lot - 1: never drink
	smoking = models.CharField()#consider changing type #yes. #no, but okay. #no, not okay.
	sleepTime = models.CharField() #early riser #night owl
	durationOfStayMonths = models.PositiveIntegerField()
	interests = models.CharField(max_length=1000)

class Building(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	contactInfo = models.CharField(max_length=255)
	distanceToCity = models.BooleanField()
	distanceToEast = models.BooleanField()
	available = models.BooleanField()
	def __str__(self):
		return self.name

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
	nickname = models.CharField(max_length=255)
	rating = models.PositiveIntegerField() #derived from reviews
	building = models.ForeignKey(Building)
	amenities = models.ManyToManyField(Amenities)
	description = models.TextField()
	price = models.IntegerField()
	leasingOptions = models.CharField()
	bedrooms = models.CharField()
	def __str__(self):
		return self.nickname

class Reviews(models.Model):
	apartment = models.ForeignKey(Building)
	comment = models.CharField(max_length=1000)
	hospitality = models.PositiveIntegerField() 
	maintenance = models.PositiveIntegerField()
	safety_security = models.PositiveIntegerField()
	overall = models.PositiveIntegerField()
	def __str__(self):
		return "%s" % self.overall