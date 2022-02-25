from django.forms import fields
from rest_framework import serializers

from tickets.models import SeatTicket, Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ['created_date', 'updated_date']


class SeatTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatTicket
        exclude = ['created_date', 'updated_date']
