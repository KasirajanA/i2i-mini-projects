from django.db import models

from shows.models import Show


class Seat(models.Model):
    """"
    Represents entity Seat in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 09/02/2022
    Date last modified: 09/02/2022
    """

    price = models.FloatField()
    show = models.ForeignKey(Show, on_delete = models.CASCADE)
    seat_reference = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "seat"

