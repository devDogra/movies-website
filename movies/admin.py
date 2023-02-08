from django.contrib import admin
from movies.models import Actor
from movies.models import Movie 
from movies.models import ActsIn

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(ActsIn)
# Register your models here.
