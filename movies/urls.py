# from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from movies import views
from movies import views


urlpatterns = [
    # path(r'^api/v1/movies/<int:pk>/', MovieDetails.as_view()),
    # url(r'api/v1/movies/<int::pk>/', MovieDetails.as_view())
 

    # path(r'^api/v1/movies2/', views.MovieDetails),

    path('movies/', views.MovieViewSet.as_view()),
    path('movies/<int:pk>/', views.MovieDetails.as_view()),
    path('actors/', views.ActorViewSet.as_view()),

   
]
