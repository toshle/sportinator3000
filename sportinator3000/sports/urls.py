from django.conf.urls import url

from sports import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^sports', views.sports, name='sports'),
    url(r'^search', views.search, name='search'),
    url(r'^raw/search', views.search_content, name='search_content'),
    url(r'^raw/sports', views.sports_content, name='sports_content'),
    url(r'^raw/home', views.home_content, name='home_content'),
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^register', views.user_register, name='register'),
    url(r'^edit', views.user_edit, name='edit'),
    url(r'^forgotten', views.user_forgotten, name='forgotten'),
    url(r'^about', views.about, name='about'),
    url(r'^api/all', views.all_places, name='all_places'),
    url(r'^api/filter', views.filters, name='filters'),
    url(r'^raw/about', views.about_content, name='about_content'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.user_profile, name='profile'),
    url(r'^details/(?P<place_id>[0-9]+)/$', views.place_details,
        name='place_details'),
    url(r'^raw/profile/(?P<user_id>[0-9]+)/$',
        views.user_profile_content, name='profile_content'),

]
