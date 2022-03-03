from django.db import models

from conferencehall.models import ConfernceHall

class Slot(models.Model):

    start_time = models.TimeField()
    end_time = models.TimeField()
    hall = models.ForeignKey(ConfernceHall, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "slot"
