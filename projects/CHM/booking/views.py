import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from booking.models import Booking
from booking.serializers import BookingSerializers
from slot.models import Slot

logger = logging.getLogger(__name__)


@api_view(['DELETE'])
def cancel_booking(request, id):
    """
    Cancel the booking using booking id

    Parameters:
    request - Http Request
    Returns:
    response
    """

    try:
        booking = Booking.objects.get(id=id)
        slot = Slot.objects.get(id=booking.slot_id.id)
        slot.booking_status = "available"
        slot.save()
        booking.delete()
        return Response("deleted")
    except Exception as exception:
        logger.exception(exception)
        return Response('Invalid Id')


@api_view(['GET'])
def get_bookings_by_employee_id(request, id):
    """
    Fetches all the details of the bookings based on employee id

    Parameters:
    request - Http Request
    Returns:
    response
    """            

    try:
        bookings = Booking.objects.filter(employee_id=id)
        if not bookings:
            return Response("No data to show")
        return Response({'bookings': bookings, 'employee_id': id})
    except Exception as exception:
        logger.exception(exception)
        return Response('Invalid Id')


@api_view(['GET'])
def get_bookings(request):
    """
    Fetches all the details of the bookings

    Parameters:
    request - Http Request
    Returns:
    response
    """
  
    try:
        bookings = Booking.objects.all
        if not bookings:
            return Response("No data to show")
        return Response(bookings)
    except Exception as exception:
        logger.exception(exception)
        return Response("Error occured")


def add_booking(request):
    """
    Creates a booking 

    Parameters:
    request - Http Request
    Returns:
    response
    """
   
    if not request.data:
       return Response("No data to create")
    try:
        booking_data = request.POST
        serializer_class = BookingSerializers
        serializer = serializer_class(data=booking_data)
        serializer.is_valid(raise_exception=True)

        slot_id = booking_data.get("slot_id")
        slot = Slot.objects.get(id=slot_id)
        if slot.booking_status == 'available':
            serializer.save()
            slot.booking_status = 'booked'
            slot.save()
            logger.info("booking created")
            return Response("Hall Booked")
        else:
            return Response("Slot unavailable")

    except Exception as exception:
        logger.exception(exception)
        return Response("Error Occured")                       