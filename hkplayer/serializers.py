from rest_framework import serializers

from . import models


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


class MovieSerializer(serializers.ModelSerializer):
    # song_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'movie_id',
            'name',
        )
        model = models.Movie




