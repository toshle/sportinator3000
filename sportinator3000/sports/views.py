from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
import math
from sports.models import Place
from simplejson import *

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

<<<<<<< HEAD
    context = []
    for place in close_places:
        json_place = {
            'name' : place.name
            'latitude' : place.latitude
            'longitude' : place.longitude
            'description' : place.description
            'address' : place.address
            'city' : place.city
            'photo_url' : place.photo_url
            'video_url' : place.video_url
            'date_added' : place.date_added}
        context.append(json_place)

    return render(request, 'sports/nearby.html', simplejson.dumps(context))
=======
        # Convert latitude and longitude to 
        # spherical coordinates in radians.
        degrees_to_radians = math.pi/180.0

        # phi = 90 - latitude
        phi1 = (90.0 - latitude1)*degrees_to_radians
        phi2 = (90.0 - latitude2)*degrees_to_radians

        # theta = longitude
        theta1 = longitude1*degrees_to_radians
        theta2 = longitude2*degrees_to_radians

        # Compute spherical distance from spherical coordinates.

        # For two locations in spherical coordinates 
        # (1, theta, phi) and (1, theta, phi)
        # cosine( arc length ) = 
        #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
        # distance = rho * arc 

        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
               math.cos(phi1)*math.cos(phi2))
        arc = math.acos( cos )

        # Remember to multiply arc by the radius of the earth 
        # in your favorite set of units to get length.
        return arc*6373
>>>>>>> 635562a373b13df05c28ab5f2ffb62b7cd6d5ddc
