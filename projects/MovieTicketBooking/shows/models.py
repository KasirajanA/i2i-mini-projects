from django.db import models

from movies.models import Movie
from screens.models import Screen


class Show(models.Model):
    """"
    Represents entity Show in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 09/02/2022
    Date last modified: 09/02/2022
    """

    show_date = models.DateField()
    show_category = models.ForeignKey('ShowCategory', on_delete=models.CASCADE) 
    screen = models.ForeignKey(Screen, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "movie_show"


class ShowCategory(models.Model):
    """"
    Represents entity Show Category in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 24/02/2022
    Date last modified: 24/02/2022
    """

    type = models.CharField(max_length=50)
    show_time = models.TimeField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "show_category"