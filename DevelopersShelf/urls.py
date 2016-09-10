from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^', include('cQuiz.urls')),
    url(r'^player/', include('hkplayer.urls')),
    url(r'^admin/', admin.site.urls),
]
