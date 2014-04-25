from django.conf.urls import url

from sports import views


urlpatterns = [
  url(r'^$', views.home, name = 'home'),
]