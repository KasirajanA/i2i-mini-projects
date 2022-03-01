import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from company.models import Company
from company.serializers import CompanySerializers

logger = logging.getLogger(__name__)


serializer_class = CompanySerializers

@api_view(['GET'])
def fetch_companies(request):
    """
    Fetches all the details of the companies

    Parameters:
    request - Http Request
    Returns:
    response
    """
    companies = Company.objects.all()
    if not companies:
        return Response("No data to show")
    return Response(companies)
            

@api_view(['POST'])
def add_company(request):
    """
    Creates a company object 

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
def delete_company(request, id):
    """
    Deletes the requested company object by id

    Parameters:
    request - Http Request
    id - company id
    Returns:
    response
    """

    try: 
        company = Company.objects.get(id=id)
        company.delete()
    except Company.DoesNotExist:
        return Response("Company id does not exists")     
    return Response("deleted")  
     

@api_view(['PUT'])
def update_company(request, id):
    """
    updates the company details 

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
            instance = Company.objects.get(id = id)
            serializer = serializer_class(instance, data = request.data)
            serializer.is_valid(raise_exception=True) 
            serializer.save()
        except Company.DoesNotExist:
            return Response("Company id does not exists")               
    return Response('success')