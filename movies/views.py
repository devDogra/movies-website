from django.shortcuts import render

from rest_framework import viewsets, generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Movie, Actor, ActsIn
from .serializers import MovieSerializer, ActorSerializer

from django.http.response import JsonResponse


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ActorViewSet(APIView):
    def get(self, request, format=None):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return JsonResponse(serializer.data, safe=False)

class MovieViewSet(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

class MovieDetails(APIView):
    def get_movie(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, safe=False)
    def patch(self, request, pk, format=None):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

