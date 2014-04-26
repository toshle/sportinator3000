from django.conf.urls import url

from sports import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^sports', views.sports, name='sports'),
    url(r'^raw/sports', views.sports_content, name='sports_content'),
    url(r'^raw/home/', views.home_content, name='home_content'),
    url(r'^api', views.nearby, name='nearby'),
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^register_form', views.user_register_form, name='register_form'),
    url(r'^register', views.user_register, name='register'),
    url(r'^about', views.about, name = 'about'),
    url(r'^raw/about', views.about_content, name = 'about_content'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.user_profile, name = 'profile'),
    url(r'^raw/profile/(?P<user_id>[0-9]+)/$', views.user_profile_content, name = 'profile_content'),
]