from django.db import models

from company.models import Company

class ConfernceHall(models.Model):
    """
    Represents the conference hall entity
    """

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    capacity = models.IntegerField()
    company_id = models.ForeignKey(Company, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
