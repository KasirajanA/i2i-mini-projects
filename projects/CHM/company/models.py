from django.db import models

class Company(models.Model):
    """
    Represents the company entity
    """

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    