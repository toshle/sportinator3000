from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse

def home(request):
  return render(request, 'sports/home.html', {})

def home_content(request):
  return render(request, 'sports/home_content.html', {})