from rest_framework import serializers

from conferencehall.models import ConfernceHall

class ConferenceHallSerializers(serializers.ModelSerializer):

    class Meta:
        model = ConfernceHall
        exclude = ['created_at', 'updated_at']
