from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

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


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

    @detail_route(methods=['get'])
    def songs(self, request, pk=None):
        self.pagination_class.page_size = 1
        songs = models.Song.objects.filter(movie_id=pk)

        page = self.paginate_queryset(songs)
        if page is not None:
            serializer = serializers.SongSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.SongSerializer(songs, many=True)
        return Response(serializer.data)


class SongViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer


