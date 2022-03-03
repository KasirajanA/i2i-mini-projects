import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from slot.models import Slot
from slot.serializers import SlotSerializers


logger = logging.getLogger(__name__)

serializer_class = SlotSerializers            
   
@api_view(['GET'])
def fetch_slots(request):
    """
    Fetches all the details of the slots

    Parameters:
    request - Http Request
    Returns:
    response
    """
    slots = Slot.objects.values()
    if not slots:
        logger.info("No Slots present")
        return Response("No data to show")
    return Response(slots)
            

@api_view(['POST'])
def add_slots(request):
    """
    Creates a slot object 

    Parameters:
    request - Http Request
    Returns:
    response
    """

    if not request.data:
        logger.warning("No data received")
        return Response("No data to create")
    serializer = serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    logger.info("Slot created")
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_slot(request, id):
    """
    Deletes the requested slot object by id

    Parameters:
    request - Http Request
    id - slot id
    Returns:
    response
    """
    try: 
        slot = Slot.objects.get(id=id)
        slot.delete()
        logger.info("Slot deleted")
    except Slot.DoesNotExist:
        logger.warning("Slot id does not exists")
        return Response("Slot id does not exists")     
    return Response("deleted")  
     

@api_view(['PUT'])
def update_slot(request, id):
    """
        update a slot object 

        Parameters:
        request - Http Request
        id - slot id
 
        Returns:
        response
        """  
    if not request.data:
        logger.warning("No data received")
        return Response("No data to update")
    else:
        try:     
            instance = Slot.objects.get(id = id)
            serializer = serializer_class(instance, data = request.data)
            serializer.is_valid(raise_exception=True)  
            serializer.save()
            logger.info("Slot updated")
        except Slot.DoesNotExist:
            logger.warning("Slot id does not exists")
            return Response("Slot id does not exists")               
    return Response('success')   

