from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


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
            return render(request, 'sports/home.hmtl', {})
        else:
            return render(request, 'sports/register.html',
                          {'disabled_account': 'Disabled account'})
    else:
        return render(request, 'sports/register.html', {})
