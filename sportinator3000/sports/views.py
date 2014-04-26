from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import math
from sports.models import Place, PlaceActivity, Activity, Sport
import json


def home(request):
    return render(request, 'sports/home.html', {})


def home_content(request):
    return render(request, 'sports/home_content.html', {})


def sports(request):
    return render(request, 'sports/sports.html', {})


def sports_content(request):
    return render(request, 'sports/sports_content.html', {})


def about(request):
    return render(request, 'sports/about.html', {})


def about_content(request):
    return render(request, 'sports/about_content.html', {})


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    notifications = []
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'sports/home.html', {})
        else:
            notifications.append(username + " акаунтът е неактивен.")
    else:
        notifications.append("Невалидно име или парола.")
        return render(request, 'sports/home.html', {'messages': notifications})


def user_logout(request):
    logout(request)
    return render(request, 'sports/home.html', {})


def user_register_form(request):
    notifications = []
    if request.user.is_authenticated():
        notifications.append("Вече сте логнат.")
        return render(request, 'sports/home.html', {'messages': notifications})
    return render(request, 'sports/register.html', {})


def user_register(request):
    notifications = []
    if request.user.is_authenticated():
        notifications.append("Вече сте логнат.")
        return render(request, 'sports/home.html', {'messages': notifications})
    user = User.objects.create_user(request.POST['username'],
                                    request.POST['email'],
                                    request.POST['password'])
    notifications.append("Регистрирахте се успешно.")
    return render(request, 'sports/home.html', {'messages': notifications})


def sport_register_form(request):
    sport = Sport(request.POST['name'], request.POST['photo_url'])
    sport.save()
    return render(request, 'sports/home.html', {})


def place_register_form(request):
    place = Place(request.POST['name'], request.POST['city'],
                  request.POST['address'], request.POST['photo_url'],
                  request.POST['video_url'], request.POST['latitude'],
                  request.POST['longitude'], request.POST['description'],
                  request.POST['date_added'])
    place.save()
    return render(request, 'sports/place_detail.html', {})


def place_activity_register_form(request):
    place_activity = PlaceActivity(Place.objects.get(id=request.POST['place']),
                                   Activity(Sport.objects
                                            .get(id=request.POST['sport']),
                                            request.POST['activity_name'],
                                            request.POST['has_trainer'],
                                            request.POST['price'],
                                            request.POST['duration'],
                                            request.POST['worktime']))
    place_activity.save()
    return render(request, 'sports/place_activity_detail.html', {})


def nearby(request):
    latitude1 = request.POST['latitude']
    longitude1 = request.POST['latitude']
    radius = request.POST['radius']

    def distance_between_points(latitude1, longitude1, latitude2, longitude2):
        degrees_to_radians = math.pi/180.0
        phi1 = (90.0 - latitude1)*degrees_to_radians
        phi2 = (90.0 - latitude2)*degrees_to_radians
        theta1 = longitude1*degrees_to_radians
        theta2 = longitude2*degrees_to_radians
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
               math.cos(phi1)*math.cos(phi2))
        arc = math.acos(cos)

        return arc*6373

    close_places = [place for place in Place.objects.all()
                    if self.distance_between_points(latitude1, longitude1,
                                                    place.latitude,
                                                    place.longitude) <= radius]

    context = []
    for place in close_places:
        json_place = {
            'name': place.name,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'description': place.description,
            'address': place.address,
            'city': place.city,
            'photo_url': place.photo_url,
            'video_url': place.video_url,
            'date_added': place.date_added}
        context.append(json_place)

def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'sports/profile.html', {'user': user})

def user_profile_content(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'sports/profile_content.html', {'user': user})