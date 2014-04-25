from django.db import models

class Activity(models.Model):
    sport = models.ForeignKey(Sport)
    name = models.CharField(max_length=200)
    has_trainer = models.BooleanField()
    price = models.FloatField()
    duration = models.IntegerField()
    worktime = models.CharField(max_length=50)
