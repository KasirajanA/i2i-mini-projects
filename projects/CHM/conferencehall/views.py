import logging

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from conferencehall.forms import ConferenceHallForm
from conferencehall.models import ConfernceHall
from conferencehall.serializers import ConferenceHallSerializers

logger = logging.getLogger(__name__)      

serializer_class = ConferenceHallSerializers

@api_view(['GET'])
def fetch_conference_halls(request):
    """
    Fetches the details of all conference halls from database 

    Parameters:
    request - Http Request
    Returns:
    response
    """

    confernce_hall = ConfernceHall.objects.all()
    if not confernce_hall:
        return Response("No data to show")
    return Response(confernce_hall)
            

@api_view(['POST'])
def add_conference_hall(request):
    """
    Creates a new conference hall object and stores in database

    Parameters:
    request - Http Request
    Returns:
    response
    """

    if not request.data:
       return Response("No data to create")
    serializer = serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_conference_hall(request, id):
    """
    deletes the hall details by the Id provided

    Parameters:
    request - Http Request
    id - conference hall id
    Returns:
    response
    """

    try: 
        confernce_hall = ConfernceHall.objects.get(id=id)
        confernce_hall.delete()
    except ConfernceHall.DoesNotExist:
        return Response("Conference hall id does not exists")     
    return Response("deleted")  
     

@api_view(['PUT'])
def update_conference_hall(request, id): 
    """
    updates the conference hall details 

    Parameters:
    request - Http Request
    id - company id
    Returns:
    response
    """

    if not request.data:
        return Response("No data to update")
    else:
        try:     
            instance = ConfernceHall.objects.get(id = id)
            serializer = serializer_class(instance, data = request.data)
            serializer.is_valid(raise_exception=True) 
            serializer.save()
        except ConfernceHall.DoesNotExist:
            return Response("Conference hall id does not exists")               
    return Response('success')            