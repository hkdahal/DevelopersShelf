from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'movie_id',
            'name'
        )
        model = models.Movie


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'artists',
            'song_link',
            'track_num'
        )
        model = models.Song

