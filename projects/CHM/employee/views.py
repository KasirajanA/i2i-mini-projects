import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from employee.models import Employee


logger = logging.getLogger(__name__)  
             
@api_view(['GET'])
def fetch_employees(request):
    """
    Fetches all the details of the employees

    Parameters:
    request - Http Request
    Returns:
    response
    """

    employees = Employee.objects.values()
    if not employees:
        logger.info("No employees present")
        return Response("No data to show")
    return Response(employees)            


@api_view(['DELETE'])
def remove_employee(request, id):
    """
    Deletes the requested employee object by id

    Parameters:
    request - Http Request
    id - employee id
    Returns:
    response
    """

    try: 
        employee = Employee.objects.get(id=id)
        employee.delete()
        logger.info("Employee removed")
    except Employee.DoesNotExist:
        logger.warning("Employee id does not exists")
        return Response("Employee id does not exists")     
    return Response("deleted")     