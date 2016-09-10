from django.shortcuts import get_object_or_404

from rest_framework import generics

from . import models
from . import serializers


class ListCreateMovie(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class RetrieveUpdateDestroyMovie(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class ListCreateSong(generics.ListCreateAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer

    def get_queryset(self):
        return self.queryset.filter(movie_id=self.kwargs.get('movie_pk'))

    def perform_create(self, serializer):
        movie = get_object_or_404(
            models.Movie, pk=self.kwargs.get('movie_pk'))
        serializer.save(movie=movie)


class RetrieveUpdateDestroySong(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer

    def get_object(self):
        return get_object_or_404(
            self.queryset,
            movie_id=self.kwargs.get('movie_pk'),
            pk=self.kwargs.get('pk')
        )

