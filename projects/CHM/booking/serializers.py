from rest_framework import serializers

from booking.models import Booking

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ['created_at', 'updated_at']