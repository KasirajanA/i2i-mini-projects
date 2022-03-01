from django.db import models

from employee.models import Employee
from slot.models import Slot

class Booking(models.Model):

    team_name = models.CharField(max_length=50)
    members = models.IntegerField()
    slot_id = models.ForeignKey(Slot, on_delete = models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
