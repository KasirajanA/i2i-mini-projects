import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from tickets.serializers import TicketSerializer
from tickets.serializers import SeatTicketSerializer
from tickets.models import Ticket


logger = logging.getLogger(__name__)

@api_view(['GET'])
def fetch_tickets(request, customer_id):
    """
    Gets a lists of tickets details that present in 
    the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    tickets = Ticket.objects.filter(customer_id=customer_id).all()

    if not tickets:
        return Response("Ticket Data is Empty")
            
    return Response(tickets)


@api_view(['DELETE'])
def delete_ticket(request, id):
    """
    Deletes a Ticket in the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    try:
        ticket = Ticket.objects.filter(id=id).all()
        ticket.delete() 
    except Ticket.DoesNotExist:
        logger.error("Ticket Id does Not Exist")
        return Response("Ticket Id does Not Exist")        
    return Response("Deleted")      


@api_view(['POST'])
def add_ticket(request):
    """
    Generates Tickets for the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """
    
    ticket_data = request.data

    if not ticket_data:
        logger.error("No Data to Generate Ticket")
        return Response("No Data to Generate Ticket")

    try:
        customer_id = ticket_data.get("customer_id")
        seats = ticket_data.getlist('tickets')
        show_id = ticket_data.get('show_id')
        price = ticket_data.get('price')
        seat_count = len(seats)
        total_price = float(price) * seat_count

        serializer_class = TicketSerializer
        serializer = serializer_class(data = dict(customer = customer_id, 
                            show = show_id, seat_count = seat_count, 
                            total_price = total_price))
        
        if not serializer.is_valid():
            serializers.ValidationError("Missing Field for Ticket Booking")

        ticket = serializer.save()

        for seat_id in seats:
            ticket_serializer = SeatTicketSerializer(data = dict(seat = seat_id, 
                                                                 ticket = ticket.id))
            if not ticket_serializer.is_valid():
                serializers.ValidationError("Missing Fields for SeatTicket")
            ticket_serializer.save()
            
            logger.info("Ticket Generated")
            return Response("Ticket Generated")
    except AssertionError:
        logger.error("Data given for Ticket is Invalid")
        return Response("Data given for Ticket is Invalid")



