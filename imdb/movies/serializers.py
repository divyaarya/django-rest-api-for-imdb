from rest_framework import serializers

from movies.models import Movies, Genre


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movies
        fields = ('popularity_index', 'director', 'genre', 'imdb_score', 'name')