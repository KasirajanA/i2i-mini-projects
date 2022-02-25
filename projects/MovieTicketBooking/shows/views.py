import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from movies.models import Movie
from screens.models import Screen
from shows.models import Show, ShowCategory
from shows.serializers import ShowCategorySerializer, ShowSerializer
from theatres.models import Theatre


logger = logging.getLogger(__name__)

@api_view(['GET'])
def fetch_shows(request):
    """
    Gets a lists of shows details that present in 
    the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    List of Shows data as Response.
    """

    shows = Show.objects.values()

    if not shows:
        logger.warning("Shows Data is Empty")
        return Response("Shows Data is Empty")
            
    return Response(shows)


@api_view(['DELETE'])
def delete_show(request, id):
    """
    Deletes a Show in the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    try:
        show = Show.objects.get(id=id)
        show.delete() 
    except Show.DoesNotExist:
        logger.error("Show Id does Not Exist")
        return Response("Show Id does Not Exist")        
    return Response("Deleted")


@api_view(['POST'])
def add_show(request):
    """
    Adds new Shows to the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Add Show")
        return Response("No Data to Add Show")

    serializer = ShowSerializer(data=request.data)

    if not serializer.is_valid():
        logger.warning("Missing Fiels While Updating Shows")
        raise serializers.ValidationError("Missing Fiels While Updating Shows")
    serializer.save()

    logger.info("New Show Created")
    return Response('Show Created')


@api_view(['PUT'])
def update_show(request, id):
    """
    Get the Show Details and Update it.

    Parameters:
    Request
    id - ShowId

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Update Show")
        return Response("No Data to Update Show")

    try:
        show = Show.objects.get(id=id)
        serializer = ShowSerializer(show, data=request.data)
        if not serializer.is_valid():
            logger.warning("Missing Fiels While Updating Shows")
            raise serializers.ValidationError("Missing Fiels While Updating Shows")
        serializer.save()
    except Show.DoesNotExist:
        logger.error("Show Id does not exists")
        return Response("Show Id does not exists")
    return Response('Show Updated')


@api_view(['GET'])
def fetch_show_category(request):
    """
    Gets a lists of show category details that present in 
    the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    List of Show Category as Response
    """

    show_category = ShowCategory.objects.values()

    if not show_category:
        logger.warning("Show Category Data is Empty")
        return Response("Show Category Data is Empty")
            
    return Response(show_category)


@api_view(['DELETE'])
def delete_show_category(request, id):
    """
    Deletes a Show Category in the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    try:
        show_category = ShowCategory.objects.get(id=id)
        show_category.delete() 
    except ShowCategory.DoesNotExist:
        logger.error("Show Category Id does Not Exist")
        return Response("Show Category Id does Not Exist")        
    return Response("Deleted")


@api_view(['POST'])
def add_show_category(request):
    """
    Adds new Show Category to the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Add Show Category")
        return Response("No Data to Add Show Category")

    serializer = ShowCategorySerializer(data=request.data)

    if not serializer.is_valid():
        logger.warning("Missing Fiels While Updating Show Category")
        raise serializers.ValidationError("Missing Fiels While Updating Show Category")
    serializer.save()

    logger.info("New Show Category Created")
    return Response('Show Category Created')


@api_view(['PUT'])
def update_show_category(request, id):
    """
    Get the Show Category Details and Update it.

    Parameters:
    Request
    id - ShowCategoryId

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Update Show Category")
        return Response("No Data to Update Show Category")

    try:
        show_category = ShowCategory.objects.get(id=id)
        serializer = ShowCategorySerializer(show_category, data=request.data)
        if not serializer.is_valid():
            logger.warning("Missing Fiels While Updating Shows Category")
            raise serializers.ValidationError("Missing Fiels While Updating Show Category")
        serializer.save()
    except ShowCategory.DoesNotExist:
        logger.error("Show Category Id does not exists")
        return Response("Show Category Id does not exists")
    return Response('Show Category Updated')


@api_view(['GET'])
def fetch_available_shows(request, customer_id):
    """
    Gets a lists of shows details that present in 
    the Movie Ticket Booking System to user to select details.

    Parameters:
    Request

    Returns:
    List of D
    """

    shows = Show.objects.values()
    screens = Screen.objects.values()
    movies = Movie.objects.values()
    theatres = Theatre.objects.values()
    show_category = ShowCategory.objects.values()
 
    response_object = dict({"shows": shows, "screens": screens, "movies": movies, 
                            "theatres": theatres, "show_category": show_category, 
                            "customer_id": customer_id})

    for value in response_object.values():
        if not value:
            logger.error("Sufficient Details Added Yet..")
            return Response("Sorry for Inconvenience Casued Sufficient Details Added Yet..")

    return Response(response_object)
    
    
    
