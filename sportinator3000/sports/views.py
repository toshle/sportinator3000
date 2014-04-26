from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
import math

def home(request):
    return render(request, 'sports/home.html', {})

def home_content(request):
    return render(request, 'sports/home_content.html', {})

def sports(request):
    return render(request, 'sports/sports.html', {})

def sports_content(request):
    return render(request, 'sports/sports_content.html', {})

def nearby(request):
    pass

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
    return render(request, 'sports/homer.html', {})

def get_distance(request):
    def distance_between_points(latitude1, longitude1, latitude2, longitude2): #returns distance in kilometers

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
