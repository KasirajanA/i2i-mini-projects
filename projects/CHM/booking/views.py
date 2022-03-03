import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from booking.models import Booking
from booking.serializers import BookingSerializers


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
        booking.delete()
        logger.info("Booking Cancelled")
        return Response("deleted")
    except Booking.DoesNotExist:
        logger.warning("Booking id does not exists")
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

    bookings = Booking.objects.values().filter(employee=id)
    if not bookings:
        logger.info("No Booking records to show")
        return Response("No data to show")
    return Response(bookings)


@api_view(['GET'])
def get_bookings(request):
    """
    Fetches all the details of the bookings

    Parameters:
    request - Http Request
    Returns:
    response
    """

    bookings = Booking.objects.values()
    if not bookings:
        logger.info("No Booking records to show")
        return Response("No data to show")
    return Response(bookings)


@api_view(['POST'])
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

    booking_data = request.data
    if Booking.objects.filter(
        booking_date=booking_data['booking_date'], slot=booking_data['slot']):
        logger.info("Slot unavailable")
        return Response("Slot unavailable")

    serializer_class = BookingSerializers
    serializer = serializer_class(data=booking_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    logger.info("Hall booked successfully")
    return Response("Hall Booked")
