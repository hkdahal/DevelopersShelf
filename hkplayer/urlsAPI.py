from django.conf.urls import url

from . import viewsAPI


urlpatterns = [
    url(r'^$', viewsAPI.ListCreateMovie.as_view(), name='movie_list'),

    url(r'^(?P<pk>\d+)/$',
        viewsAPI.RetrieveUpdateDestroyMovie.as_view(),
        name="movie_detail"),

    url(r'^(?P<movie_pk>\d+)/songs/$',
        viewsAPI.ListCreateSong.as_view(),
        name='song_list'),

    url(r'^(?P<movie_pk>\d+)/songs/(?P<pk>\d+)/$',
        viewsAPI.RetrieveUpdateDestroySong.as_view(),
        name='song_detail'
        )
]

