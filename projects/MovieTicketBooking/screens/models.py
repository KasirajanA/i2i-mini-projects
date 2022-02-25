from django.db import models

from theatres.models import Theatre


class Screen(models.Model):
    """"
    Represents entity Screen in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 09/02/2022
    Date last modified: 09/02/2022
    """

    type = models.CharField(max_length = 20)
    theatre = models.ForeignKey(Theatre, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "screen"