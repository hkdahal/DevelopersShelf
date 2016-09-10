from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=1000)
    movie_id = models.IntegerField(default=0)

    def __str__(self):
        return "{0}. {1}".format(self.movie_id, self.name)


class Song(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    artists = models.CharField(max_length=1000)
    song_link = models.CharField(max_length=1000)
    track_num = models.IntegerField(default=0)

    def __str__(self):
        return "Track#{0} Song: '{1}' of {2}".format(self.track_num, self.title, self.movie)
