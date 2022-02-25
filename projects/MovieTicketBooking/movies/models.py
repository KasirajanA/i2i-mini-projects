from django.db import models


class Movie(models.Model):
    """"
    Represents entity Movies in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 08/02/2022
    Date last modified: 08/02/2022
    """

    name = models.CharField(max_length = 20)
    language = models.CharField(max_length = 20)
    genre = models.CharField(max_length = 20)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "movie"