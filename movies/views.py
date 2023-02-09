from django.shortcuts import render

from rest_framework import viewsets

from .models import Movie, Actor, ActsIn
from .serializers import MovieSerializer, ActorSerializer


# Create your views here.
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ActorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer