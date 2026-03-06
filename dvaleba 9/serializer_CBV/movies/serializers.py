from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    movie_id = serializers.PrimaryKeyRelatedField(source='movie', queryset=Movie.objects.all(), write_only=True)
    movie = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'created_at']


class MovieSerializer(serializers.ModelSerializer):
    director_id = serializers.PrimaryKeyRelatedField(source='director', queryset=Director.objects.all(), write_only=True)
    director = DirectorSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'