from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # cQuiz
    url(r'^', include('cQuiz.urls')),

    # Music Player
    url(r'^player/', include('hkplayer.urls')),

    # Admin
    url(r'^admin/', admin.site.urls),

    # REST Framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API
    url(r'api/v1/movies/', include('hkplayer.urlsAPI', namespace="movies")),
]
