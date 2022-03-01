import logging

from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response

from company.models import Company
from employee.models import Employee
from employee.serializers import EmployeeSerializers

logger = logging.getLogger(__name__)


@api_view(['POST'])
def employee_login(request):
    """
    gets login data validates the user

    Parameters:
    request - Http Request
    Returns:
    response
    """

    if not request.data:
        return Response("No data found")
    try:
        employee_data = Employee.objects.get(email = request.data.get("email"))
        if check_password(request.data.get('password'), employee_data.password):
            return Response("Success")
        else:
            print(request.data.get('password'))
            return Response("Password does not match")
    except Exception as exception:
        logger.exception(exception)
        return Response("Email does not exist")


@api_view(['POST'])
def employee_registration(request):
    """
    Registers an employee

    Parameters:
    request - Http Request
    Returns:
    response
    """

    if not request.data:
        return Response("No data found")
    try:
        if request.data.get("password1") != request.data.get("password2"):
            return Response('Password does not match')    
                
        
        if Employee.objects.filter(email = request.data['email']).exists():
            return Response('Email already exists')                      
        else:
            company = Company.objects.get(name= request.data['company'])
            emp = dict(name = request.data['name'], email = request.data['email'],
                company = company.id,
                password = make_password(request.data['password1'])) 
            serializer_class = EmployeeSerializers
            serializer = serializer_class(data=emp)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Registered successfully")
            
    except Exception as exception:
        logger.exception(exception)
        return Response("Cannot register")      