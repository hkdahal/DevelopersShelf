from django.conf.urls import url

from . import viewsAPI

urlpatterns = [
    url(r'^$', viewsAPI.ListCreateMovie.as_view(), name='movie_list')
]