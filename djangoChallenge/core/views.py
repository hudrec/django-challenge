from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from core.models import Person, Movie
from core.serializers import PersonSerializer, MovieSerializer

# Create your views here.


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer