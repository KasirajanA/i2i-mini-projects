import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from seats.models import Seat
from seats.serializers import SeatSerializer
from tickets.models import SeatTicket


logger = logging.getLogger(__name__)

@api_view(['GET'])
def fetch_seats(request):
    """
    Gets a lists of seats of a screen that present in 
    the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    list of Seats data as Response
    """

    seats = Seat.objects.values()

    if not seats:
        logger.info("Seats Data is Empty")
        return Response("Seats Data is Empty")
            
    return Response(seats)


@api_view(['DELETE'])
def delete_seat(request, id):
    """
    Deletes a Seat in the Screen of Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    try:
        seat = Seat.objects.get(id=id)
        seat.delete() 
    except Seat.DoesNotExist:
        logger.error("Seat Id does Not Exist")
        return Response("Seat Id does Not Exist")        
    return Response("Deleted")


@api_view(['POST'])
def add_seat(request):
    """
    Adds new Seat to screen in the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Add Seat")
        return Response("No Data to Add Seat")

    serializer = SeatSerializer(data=request.data)

    if not serializer.is_valid():
        logger.warning("Missing Fiels While Updating Seat")
        raise serializers.ValidationError("Missing Fiels While Updating Seat")
    serializer.save()

    logger.info("New Seat Created")
    return Response('Seat Created')


@api_view(['PUT'])
def update_seat(request, id):
    """
    Get the Seat Details and Update it.

    Parameters:
    Request
    id - SeatId

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Update Seat")
        return Response("No Data to Update Seat")

    try:
        seat = Seat.objects.get(id=id)
        serializer = SeatSerializer(seat, data=request.data)
        if not serializer.is_valid():
            logger.warning("Missing Fiels While Updating Seat")
            raise serializers.ValidationError("Missing Fiels While Updating Seat")
        serializer.save()
    except Seat.DoesNotExist:
        logger.error("Seat Id does not exists")
        return Response("Seat Id does not exists")
    return Response('Seat Updated')

@api_view(['GET'])
def fetch_available_seats(request, show_id, customer_id):
    """
    Gets a lists of seats details that present in 
    the Movie Ticket Booking System to user to select available seats.

    Parameters:
    Request

    Returns:
    List of Available Seats as Response
    """

    booked_seats = []
    available_seats = []
    seats = Seat.objects.filter(show_id=show_id).all()

    if not seats:
        logger.warning("No seats Data Present for this Show")
        return Response("No seats Data Present for this Show")

    seat_tickets = SeatTicket.objects.all()

    if seat_tickets:
        for seat_ticket in seat_tickets:
            booked_seats.append(seat_ticket.seat_id)

    for seat in seats:
        if not seat.id in booked_seats:
            available_seats.append(dict(seat_id=seat.id, 
                    seat_reference=seat.seat_reference, seat_price= seat.price))

    return Response(available_seats)
    