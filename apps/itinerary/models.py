from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from apps.inquiries.models import Inquiry

# Create your models here.

class Guide(models.Model):
    guide_name = models.CharField('guide_name', max_length=100)
    guide_phone = models.CharField(max_length=15, default='')
    class Meta:
        verbose_name_plural = 'guides'
        db_table = 'guides'

    def __str__(self):
        return self.guide_name


class Driver(models.Model):
    driver_name = models.CharField('driver_name', max_length=100)
    driver_phone = models.CharField(max_length=15, default='')

    class Meta:
        verbose_name_plural = 'drivers'
        db_table = 'drivers'

    def __str__(self):
        return self.driver_name


class Vehicle(models.Model):
    vehicle_number = models.CharField('vehicle_number', max_length=16)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,related_name="vehicle_driver")
    class Meta:
        verbose_name_plural = 'vehicles'
        db_table = 'vehicles'

    def __str__(self):
        return self.vehicle_driver


class Itinerary(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE,related_name="itineraries")
    url = models.CharField(max_length=255)                  
    itineraryname = models.CharField(max_length=250, default='')
    numberadults = models.IntegerField()
    numberchildren = models.IntegerField()
    itinerarystatus = models.IntegerField(default=0)
    monthyear = models.DateTimeField()
    visits = models.IntegerField(default=0)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE,related_name="itineraries")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'itineraries'
        verbose_name_plural = 'itineraries'
    
    def __str__(self):
        return self.itineraryname


class Day(models.Model):
    daytype = models.IntegerField(default=0)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE,related_name='day_Itinerary', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'days'
        db_table = 'days'

    def __str__(self):
        return self.itineraryname


class Activity(models.Model):
    title = models.CharField(max_length=250, default='')
    description = models.TextField(blank=True, null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='activity_day', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'activities'
        db_table = 'activities'

    def __str__(self):
        return self.itineraryname
