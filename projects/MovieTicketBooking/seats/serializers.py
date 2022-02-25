from rest_framework import serializers

from seats.models import Seat


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        exclude = ['created_date', 'updated_date']