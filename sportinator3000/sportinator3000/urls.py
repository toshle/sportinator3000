from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sportinator3000.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('sports.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
