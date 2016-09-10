from django.conf.urls import url

from . import viewsAPI

urlpatterns = [
    url(r'^$', viewsAPI.ListCreateMovie.as_view(), name='movie_list'),
    url(r'(?P<pk>\d+)/$',
        viewsAPI.RetrieveUpdateDestroyMovie.as_view(),
        name="movie_detail"),
]
