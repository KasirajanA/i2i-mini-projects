import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from theatres.models import Theatre
from theatres.serializers import TheatreSerializer


logger = logging.getLogger(__name__)

@api_view(['GET'])
def fetch_theatres(request):
    """
    Gets a lists of theatres details that present in 
    the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    List of Theatre data as Response.
    """

    theatres = Theatre.objects.values()

    if not theatres:
        logger.warning("Theatres Data is Empty")
        return Response("Theatres Data is Empty")
            
    return Response(theatres)


@api_view(['DELETE'])
def delete_theatre(request, id):
    """
    Deletes a Theatres in the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    try:
        theatre = Theatre.objects.get(id=id)
        theatre.delete() 
    except Theatre.DoesNotExist:
        logger.error("Theatre Id does Not Exist")
        return Response("Theatre Id does Not Exist")        
    return Response("Deleted")


@api_view(['POST'])
def add_theatre(request):
    """
    Adds new Theatres to the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Add Theatre")
        return Response("No Data to Add Theatre")

    serializer = TheatreSerializer(data=request.data)
    
    if not serializer.is_valid():
        logger.warning("Missing Fiels While Updating Theatres")
        raise serializers.ValidationError("Missing Fiels While Updating Theatres")
    serializer.save()

    logger.info("New Theatre Created")
    return Response('Theatre Created')


@api_view(['PUT'])
def update_theatre(request, id):
    """
    Get the Theatre Details and Update it.

    Parameters:
    Request
    id - TheatreId

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Update Theatre")
        return Response("No Data to Update Theatre")

    try:
        theatre = Theatre.objects.get(id=id)
        serializer = TheatreSerializer(theatre, data=request.data)
        if not serializer.is_valid():
            logger.warning("Missing Fiels While Updating Theatres")
            raise serializers.ValidationError("Missing Fiels While Updating Theatres")
        serializer.save()
    except Theatre.DoesNotExist:
        logger.error("Theatre Id does not exists")
        return Response("Theatre Id does not exists")
    return Response('Theatre Updated')


