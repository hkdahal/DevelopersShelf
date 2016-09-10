from django.contrib import admin

from .models import Question, Choice

from hkplayer.models import Movie, Song

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Movie)
admin.site.register(Song)