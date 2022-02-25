from django.forms import models
from rest_framework import serializers

from shows.models import Show, ShowCategory


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        exclude = ['created_date', 'updated_date']


class ShowCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowCategory
        exclude = ['created_date', 'updated_date']