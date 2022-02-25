from django.db import models

from customer.models import Customer
from seats.models import Seat
from shows.models import Show


class Ticket(models.Model):
    """"
    Represents entity Ticket in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 15/02/2022
    Date last modified: 15/02/2022
    """

    show = models.ForeignKey(Show, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    total_price = models.FloatField()
    seat_count = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "ticket"


class SeatTicket(models.Model):
    """"
    Represents entity SeatTicket in the Movie Ticket Booking.
    
    Author: Rahul
    Date created: 16/02/2022
    Date last modified: 16/02/2022
    """

    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    # show = models.ForeignKey(Show, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "seat_ticket"