from django.db import models

from conferencehall.models import ConfernceHall

class Slot(models.Model):

    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    hall_id = models.ForeignKey(ConfernceHall, on_delete = models.CASCADE)
    booking_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
