from django.conf.urls import url

from sports import views


urlpatterns = [
  url(r'^$', views.home, name = 'home'),
  url(r'^home', views.home, name = 'home'),
  url(r'^raw/home/', views.home_content, name = 'home_content'),
]