from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.conf import settings

from NGSmethDB2020 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^browser/', include('browser.urls')),
    url(r'^results/', include('results.urls')),
    url(r'^dbcontent/', include('dbcontent.urls')),
    url(r'^$', views.index, name='home'),
]