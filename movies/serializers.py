from rest_framework import serializers

from .models import Actor, Movie, ActsIn

# will have to convert to 3 jsons cuz 
# 1 is too diff :( # or mayb not..
# #seelaptopstkovrflo.d

# class ActorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Actor
#         fields=['name', 'dateOfBirth', 'numberOfMovies']

# class MovieSerializer(serializers.ModelSerializer):
#     actors = ActorSerializer(many=True)
#     class Meta:
#         fields = ['title', 'description', 'releaseDate', 'numberOfActors','actors']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields=['name', 'dateOfBirth', 'numberOfMovies']
        

class ActsInSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActsIn
        # fields="__all__"
        fields=['movie', 'actor']
    
class MovieSerializer(serializers.ModelSerializer):
    # actors = ActorSerializer(many=True)
    # actors = ActsInSerializer(many=True)
    class Meta:
        model=Movie
        # fields = ['title', 'description', 'releaseDate', 'numberOfActors',actors]
        fields='__all__'
 
#  Read the asmt carefully, again



