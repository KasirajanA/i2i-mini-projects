import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from movies.models import Movie
from movies.serializers import MovieSerializer


logger = logging.getLogger(__name__)

@api_view(['GET'])
def fetch_movies(request):
    """
    Gets a lists of movies details that present in 
    the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    List of Movies data as Response.
    """

    movies = Movie.objects.values()

    if not movies:
        logger.warning("Movies Data is Empty")
        return Response("Movies Data is Empty")
            
    return Response(movies)


@api_view(['DELETE'])
def delete_movie(request, id):
    """
    Deletes a selected movie in the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    try:
        movie = Movie.objects.get(id=id)
        movie.delete() 
    except Movie.DoesNotExist:
        logger.error("Movie Id does Not Exist")
        return Response("Movie Id does Not Exist")        
    return Response("Deleted")


@api_view(['POST'])
def add_movie(request):
    """
    Adds new movie to the Movie Ticket Booking System.

    Parameters:
    Request

    Returns:
    Response
    """

    if not request.data:
        logger.warning("No Data to Add Movie")
        return Response("No Data to Add Movie")

    serializer = MovieSerializer(data=request.data)

    if not serializer.is_valid():
        logger.warning("Missing Fiels While Updating Movies")
        raise serializers.ValidationError("Missing Fiels While Updating Movies")
    serializer.save()

    logger.info("New Movie Created")
    return Response('Movie Created')


@api_view(['PUT'])
def update_movie(request, id):
    """
    Get the Movie Details and Update it.

    Parameters:
    Request
    id - MovieId.

    Returns:
    Response.
    """

    if not request.data:
        logger.warning("No Data to Update Movie")
        return Response("No Data to Update Movie")

    try:
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie, data=request.data)
        if not serializer.is_valid():
            logger.warning("Missing Fiels While Updating Movies")
            raise serializers.ValidationError("Missing Fiels While Updating Movies")
        serializer.save()
    except Movie.DoesNotExist:
        logger.error("Movie Id does not exists")
        return Response("Movie Id does not exists")
    logger.info('Movie Updated')
    return Response('Movie Updated')





