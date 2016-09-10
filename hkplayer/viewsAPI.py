from rest_framework import generics

from . import models
from . import serializers


class ListCreateMovie(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class RetrieveUpdateDestroyMovie(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
