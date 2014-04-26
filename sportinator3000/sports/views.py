from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import help_modules
from sports.models import Place, PlaceActivity, Activity, Sport
import json
from django.shortcuts import redirect


def home(request):
    return render(request, 'sports/home.html', {})


def home_content(request):
    return render(request, 'sports/home_content.html', {})

def search(request):
    return render(request, 'sports/search.html', {})


def search_content(request):
    return render(request, 'sports/search_content.html', {})


def all_places(request):
    return HttpResponse(content=Place.to_json(Place.get_all()))

def filters(request):
    latitude1 = float(request.GET['latitude'])
    longitude1 = float(request.GET['longitude'])
    radius = float(request.GET['radius'])

    close_places = [place for place in 
                    help_modules.filter_all(PlaceActivity.get_all(),
                                request.GET.get('sport'),
                                request.GET.get('duration'),
                                request.GET.get('price'))
                    if help_modules.distance_between_points(latitude1, longitude1,
                                                            place.place.latitude,
                                                            place.place.longitude)
                    <= radius]

    return HttpResponse(content=Place.to_json(map(lambda x: x.place, close_places)))

def sports(request):
    latitude1 = float(request.GET['latitude'])
    longitude1 = float(request.GET['longitude'])
    radius = float(request.GET['radius'])

    close_places = [place for place in 
                    help_modules.filter_all(PlaceActivity.get_all(),
                                request.GET.get('sport'),
                                request.GET.get('duration'),
                                request.GET.get('price'))
                    if help_modules.distance_between_points(latitude1, longitude1,
                                                            place.place.latitude,
                                                            place.place.longitude)
                    <= radius]

    return render(request, 'sports/sports.html',
                  {'json_places': Place.to_json(map(lambda x: x.place, close_places)),
                   'places': close_places,
                   'sports': Sport.objects.all()})


def sports_content(request):
    latitude1 = float(request.GET['latitude'])
    longitude1 = float(request.GET['longitude'])
    radius = float(request.GET['radius'])

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

    close_places = [place for place in
                    PlaceActivity.objects.filter(
                        activity__sport__id=request.GET['sport'],
                        activity__duration=request.GET['duration'],
                        activity__price__lte=request.GET['price'])
                    if distance_between_points(latitude1, longitude1,
                                               place.place.latitude,
                                               place.place.longitude)
                    <= radius]

    return render(request, 'sports/sports_content.html',
                  {'json_places': Place.to_json(close_places),
                   'places': close_places,
                   'sports': Sport.objects.all()})


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

def user_edit(request):
    notifications = []
    if request.user.is_authenticated():
        if request.user.check_password(request.POST['old_password']):
          request.user.first_name = request.POST['first_name']
          request.user.last_name = request.POST['last_name']
          new_password = request.POST['new_password']
          if new_password and new_password == request.POST['new_password_repeat']:
              request.user.set_password(new_password)
          request.user.save()
          notifications.append("Успешно редактиране.")
        else:
          notifications.append("Грешна парола.")
        return render(request, 'sports/profile.html', {'details': request.user, 'messages': notifications})
    else:
        notifications.append("Трябва да се логнете.")
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


def user_profile(request, user_id):
    notifications = []
    if request.user.is_authenticated():
        user = get_object_or_404(User, pk=user_id)
        return render(request, 'sports/profile.html', {'details': user})
    else:
        notifications.append("Не сте логнат.")
        return render(request, 'sports/home.html', {'messages': notifications})


def user_profile_content(request, user_id):
    notifications = []
    if request.user.is_authenticated():
        user = get_object_or_404(User, pk=user_id)
        return render(request, 'sports/profile_content.html', {'details': user})
    else:
        notifications.append("Не сте логнат.")
        return render(request, 'sports/home.html', {'messages': notifications})


def user_forgotten(request):
    notifications = []
    if request.user.is_authenticated():
        notifications.append("Вече сте логнат.")
        return render(request, 'sports/home.html', {'messages': notifications})
    user = User.objects.get(username=request.POST['username'],
                            email=request.POST['email'])
    new_password = hashlib.sha224(str(randint(1, 100000000))
                                  .encode('utf-8')).hexdigest()[0:6]
    user.set_password(new_password)
    user.email_user("Новата ви парола", "Новата ви парола е " + new_password)
    user.save()
    notifications.append("Изпратена ви е нова парола на " +
                         request.POST['email'])
    return render(request, 'sports/home.html', {'messages': notifications})


def place_details(request, place_id):
    notifications = []
    place = Place.objects.get(pk=place_id)
    activities = PlaceActivity.objects.filter(place_id=place_id)
    return render(request, 'sports/details.html',
                  {'place': place, 'activities': activities})
