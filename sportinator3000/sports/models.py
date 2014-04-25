from django.db import models
from datetime import datetime


CITIES = (
    ('Varna', 'Варна'),
    ('Sofia', 'София'),
    ('Plovdiv', 'Пловдив'),
    ('Stara Zagora', 'Стара Загора'),
    ('Montana', 'Монтана'),
    ('Burgas', 'Бургас'),
    ('Razgrad', 'Разград'),
    ('Ruse', 'Русе')
)


class Place(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    city        = models.CharField(max_length=30, choices=CITIES)
    address     = models.CharField(max_length=200)
    photo_url   = models.CharField(max_length=300, blank=True)
    video_url   = models.CharField(max_length=300, blank=True)
    latitude    = models.IntegerField()
    longitude   = models.IntegerField()
    description = models.TextField()
    date_added  = models.DateTimeField(default=datetime.now())

    def __str__():
        return '{}, {}, {}'.format(name, city, address)


class Sport(models.Model):
    name      = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=300, blank=True)

    def __str__():
        return '{}'.format(name)


class Activity(models.Model):
    sport       = models.ForeignKey(Sport)
    place       = models.ForeignKey(Place)
    name        = models.CharField(max_length=200)
    has_trainer = models.BooleanField()
    price       = models.FloatField()
    duration    = models.IntegerField()
    worktime    = models.CharField(max_length=50)

    def __str__():
        return '{}'.format(name)
