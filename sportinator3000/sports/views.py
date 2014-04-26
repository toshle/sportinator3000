from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import math
from sports.models import Place
import json


def home(request):
    return render(request, 'sports/home.html', {})


def home_content(request):
    return render(request, 'sports/home_content.html', {})


def sports(request):
    return render(request, 'sports/sports.html', {})


def sports_content(request):
    return render(request, 'sports/sports_content.html', {})


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'sports/home.html', {})
        else:
            return render(request, 'sports/register.html',
                          {'disabled_account': 'Disabled account'})
    else:
        return render(request, 'sports/register.html', {})


def user_logout(request):
    logout(request)
    return render(request, 'sports/home.html', {})


def user_register_form(request):
    if request.user.is_authenticated():
        return render(request, 'sports/home.html', {})
    return render(request, 'sports/register.html', {})


def user_register(request):
    if request.user.is_authenticated():
        return render(request, 'sports/home.html', {})
    user = User.objects.create_user(request.POST['username'],
                                    request.POST['email'],
                                    request.POST['password'])
    return render(request, 'sports/home.html', {})


def place_register_form(request):
    place = Place(request.POST['name'], request.POST['city'],
                  request.POST['address'], request.POST['photo_url'],
                  request.POST['video_url'], request.POST['latitude'],
                  request.POST['longitude'], request.POST['description'],
                  request.POST['date_added'])
    return render(request, 'sports/detail.html', {})


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
