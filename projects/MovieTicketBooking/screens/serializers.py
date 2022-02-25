from rest_framework import serializers

from screens.models import Screen


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        exclude = ['created_date', 'updated_date']