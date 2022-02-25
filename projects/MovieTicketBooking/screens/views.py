import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from screens.models import Screen
from screens.serializers import ScreenSerializer


logger = logging.getLogger(__name__)

@api_view(['GET'])
def fetch_screens(request):
    """
    Gets a lists of screens details that present in 
    the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    List of Screen data as Response
    """

    screens = Screen.objects.values()

    if not screens:
        logger.info("Screens Data is Empty")
        return Response("Screens Data is Empty")
            
    return Response(screens)


@api_view(['DELETE'])
def delete_screen(request, id):
    """
    Deletes a Screen in the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    try:
        screen = Screen.objects.get(id=id)
        screen.delete() 
    except Screen.DoesNotExist:
        logger.error("Screen Id does Not Exist")
        return Response("Screen Id does Not Exist")        
    return Response("Deleted")


@api_view(['POST'])
def add_screen(request):
    """
    Adds new Screen to the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Add Screen")
        return Response("No Data to Add Screen")

    serializer = ScreenSerializer(data=request.data)
    
    if not serializer.is_valid():
        logger.warning("Missing Fiels While Updating Screens")
        raise serializers.ValidationError("Missing Fiels While Updating Screens")
    serializer.save()

    logger.info("New Screen Created")
    return Response('Screen Created')


@api_view(['PUT'])
def update_screen(request, id):
    """
    Get the Screen Details and Update it.

    Parameters:
    Request
    id - ScreenId

    Returns:
    Calls the get screens method to show list of screens
    """

    if not request.data:
        logger.warning("No Data to Update Screen")
        return Response("No Data to Update Screen")

    try:
        screen = Screen.objects.get(id=id)
        serializer = ScreenSerializer(screen, data=request.data)
        if not serializer.is_valid():
            logger.warning("Missing Fiels While Updating Screens")
            raise serializers.ValidationError("Missing Fiels While Updating Screens")
        serializer.save()
    except Screen.DoesNotExist:
        logger.error("Screen Id does not exists")
        return Response("Screen Id does not exists")
    return Response('Screen Updated')


