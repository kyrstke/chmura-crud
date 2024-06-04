from django.db import models


class Circuit(models.Model):
    circuitId = models.AutoField(primary_key=True)
    circuitRef = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.CharField()
    lng = models.CharField()
    alt = models.CharField()
    url = models.CharField()
