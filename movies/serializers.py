from rest_framework import serializers

from .models import Actor, Movie, ActsIn


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields=['name', 'dateOfBirth', 'numberOfMovies']
        

class ActsInSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActsIn
        fields=['movie', 'actor']
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
 



