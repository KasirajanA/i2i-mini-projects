from django.db import models


class Theatre(models.Model):
    """"
    Represents entity Theatres in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 09/02/2022
    Date last modified: 09/02/2022
    """

    name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 50)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
 
    class Meta:
        db_table = "theatre"
