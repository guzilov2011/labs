from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    sex = models.CharField(max_length=1, default='M')
    phone = models.CharField(max_length=20, null=False, blank=False)
    #tbd
    
class Hotel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rate = models.IntegerField(default = '0')
    city = models.CharField(max_length=255, null=False, blank=False)
    street = models.CharField(max_length=255, null=False, blank=False)
    house = models.CharField(max_length=10, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    photopath = models.URLField()
    services = models.TextField(max_length=500)
    description = models.TextField(max_length=2000)
    
class Room(models.Model):
    number = models.IntegerField(max_length=4, unique=True)
    hotelname = models.CharField(max_length=511, null=False, blank=False)
    description = models.TextField(max_length=2000)
    photopath = models.URLField()
    
class Booking(models.Model):
    booking = models.IntegerField(unique=True)
    room = models.IntegerField(max_length=4, null=False, blank=False)
    datein = models.DateField(null=False, blank=False)
    dateout = models.DateField(null=False, blank=False)
    user = models.CharField(max_length=255, unique=True)

class Review(models.Model):
    user = models.CharField(max_length=255, unique=True)
    hotel = models.CharField(max_length=255, unique=True)
    datein = models.DateField(null=False, blank=False)
    dateout = models.DateField(null=False, blank=False)
    review = models.TextField(null=False, blank=False)
    mark = models.FloatField(null=False, blank=False)
    photopath = models.URLField()