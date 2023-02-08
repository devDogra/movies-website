from django.db import models

# Create your models here.

"""'
also, ids are generated implicitly
in django

MOVIE:
id, title, desc, releasedate, votes, #actors?

ACTOR:
id, name, dob, #movies?

ACTS_IN
actor_id, movie_id, 
"""
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    releaseDate = models.DateField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()

    def __str__(self):
        return self.name


class ActsIn(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.actor) + " in " + str(self.movie))

