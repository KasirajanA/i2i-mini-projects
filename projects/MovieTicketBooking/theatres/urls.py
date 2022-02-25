from django.urls import path

from theatres.views import add_theatre, delete_theatre, fetch_theatres, update_theatre


urlpatterns = [
    path('addtheatre/', add_theatre),
    path('displaytheatres', fetch_theatres),
    path('deletetheatre/<int:id>', delete_theatre),
    path('updatetheatre/<int:id>', update_theatre),
]