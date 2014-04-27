from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import json


CITIES = (
    ('Varna', 'Варна'),
    ('Sofia', 'София'),
    ('Plovdiv', 'Пловдив'),
    ('Stara Zagora', 'Стара Загора'),
    ('Montana', 'Монтана'),
    ('Burgas', 'Бургас'),
    ('Razgrad', 'Разград'),
    ('Ruse', 'Русе'),
    ('Jelezna', 'Железна')
)


class Place(models.Model):
    name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=30, choices=CITIES)
    address = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=300, blank=True)
    video_url = models.CharField(max_length=300, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    date_added = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def to_json(cls, places):
        context = []
        for place in places:
            json_place = {
                'id': place.id,
                'name': place.name,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'description': place.description,
                'address': place.address,
                'city': place.city,
                'photo_url': place.photo_url,
                'video_url': place.video_url,
                'user_id': place.user_id,
                'date_added': 'place.date_added'}
            context.append(json_place)
        return json.dumps(context)

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.city, self.address)


class Sport(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(User)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '{}'.format(self.name)


class Activity(models.Model):
    sport = models.ForeignKey(Sport)
    name = models.CharField(max_length=200)
    has_trainer = models.BooleanField(default=True)
    price = models.FloatField()
    duration = models.IntegerField()
    worktime = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '{} price {}'.format(self.name, self.price)


class PlaceActivity(models.Model):
    place = models.ForeignKey(Place)
    activity = models.ForeignKey(Activity)

    def __str__(self):
        return '{} {}'.format(self.place, self.activity)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_sport(cls, sport_name):
        return cls.objects.filter(activity__sport__name=sport_name)

    @classmethod
    def get_by_city(cls, city_name):
        return cls.objects.filter(place__city=city_name)

    @classmethod
    def get_by_sport_and_city(cls, sport_name, city_name):
        return cls.objects.filter(place__city=city_name,
                                  activity__sport__name=sport_name)

    @classmethod
    def costs_lower_than(cls, data_list, costs):
        return data_list.filter(activity__price__lte=costs)\
            .order_by('activity__price')

    @classmethod
    def order_ascending_by_price(cls, data_list):
        return data_list.order_by('activity__price')

    @classmethod
    def order_descending_by_price(cls, data_list):
        return data_list.order_by('-activity__price')
