from rest_framework import serializers
from core.models import Person, Movie
from .tasks import int_to_roman


class MovieBaseSerializer(serializers.ModelSerializer):
    release_year = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'release_year',
        ]

    def get_release_year(self, obj):
        return int_to_roman(obj.release_year)


class PersonSerializer(serializers.ModelSerializer):
    movies_as_actor = MovieBaseSerializer(many=True)
    movies_as_director = MovieBaseSerializer(many=True)
    movies_as_producer = MovieBaseSerializer(many=True)

    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'role',
            'aliases',
            'movies_as_actor',
            'movies_as_director',
            'movies_as_producer',
        ]
        depth = 2

    def get_movies(self, obj):
        return{
            'AC': MovieSerializer(obj.movies_as_actor.fields('title').all(), many=True).data,
            'DI': MovieSerializer(obj.movies_as_director.all(), many=True).data,
            'PR': MovieSerializer(obj.movies_as_producer.all(), many=True).data,
        }[obj.role]


class MovieSerializer(MovieBaseSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 2
