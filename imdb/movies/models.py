from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Movies(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    imdb_score = models.FloatField(default=0.0)
    popularity_index = models.FloatField(null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
