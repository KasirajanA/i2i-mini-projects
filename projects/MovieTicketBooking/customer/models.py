from django.db import models


class Customer(models.Model):
    """"
    Represents entity Customer in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 15/02/2022
    Date last modified: 15/02/2022
    """

    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "customer"