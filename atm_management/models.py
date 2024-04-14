from django.db import models

# Create your models here.
import json

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ATMSite(models.Model):
    name = models.CharField(max_length=255)
    site_id = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    contact_details = models.JSONField()

    def __str__(self):
        return self.name