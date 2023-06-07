from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pilot(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    total_hours = models.IntegerField()
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Balloon(models.Model):
    type = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.type} {self.manufacturer}"

class AirLine(models.Model):
    name = models.CharField(max_length=200)
    founding_year = models.IntegerField()
    eu_out = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class AirLinePilot(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(AirLine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pilot} {self.airline}"

class Flight(models.Model):
    code = models.CharField(max_length=100)
    airport_takeoff = models.CharField(max_length=255)
    airport_landing = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="flights/")
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    airline = models.ForeignKey(AirLine, on_delete=models.CASCADE)

    def __str__(self):
        return self.code