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
    name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=30, choices=CITIES)
    address = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=300, blank=True)
    video_url = models.CharField(max_length=300, blank=True)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    description = models.TextField()
    date_added = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.city, self.address)


class Sport(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Activity(models.Model):
    sport = models.ForeignKey(Sport)
    name = models.CharField(max_length=200)
    has_trainer = models.BooleanField(default=True)
    price = models.FloatField()
    duration = models.IntegerField()
    worktime = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


class PlaceActivity(models.Model):
    place = models.ForeignKey(Place)
    activity = models.ForeignKey(Activity)

    def __str__(self):
        return '{}'.format(self.place)
