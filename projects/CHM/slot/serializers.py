from rest_framework import serializers

from slot.models import Slot

class SlotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slot
        exclude = ['created_at', 'updated_at']
