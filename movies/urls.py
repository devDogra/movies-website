from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views


urlpatterns = [
    path('movies/', views.MovieViewSet.as_view()),
    path('movies/<int:pk>/', views.MovieDetails.as_view()),
    path('actors/', views.ActorViewSet.as_view()),

   
]
