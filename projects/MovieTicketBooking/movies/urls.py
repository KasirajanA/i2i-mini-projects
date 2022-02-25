from django.urls import path

from movies.views import add_movie, delete_movie, fetch_movies, update_movie


urlpatterns = [
    path('addmovie/', add_movie),
    path('displaymovies', fetch_movies),
    path('deletemovie/<int:id>', delete_movie),
    path('updatemovie/<int:id>', update_movie),
]