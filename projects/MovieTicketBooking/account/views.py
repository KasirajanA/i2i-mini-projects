import logging
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from customer.models import Customer
from customer.serializers import CustomerSerializer


logger = logging.getLogger(__name__)

@api_view(['POST'])
def register(request):
    """
    Allows user to Register in the Application.

    Parameters:
    Request

    Returns:
    Response
    """

    customer = request.data

    if not customer:
        logger.info("No Data to Add Movie")
        return Response("No Data to Add Movie")

    if customer.get("password1") != customer.get("password2"):
        logger.warning("Password Doesn't  Match")
        return Response("Password Doesn't  Match")
    
    if Customer.objects.filter(username=customer.get('username')):
        logger.warning("UserName Already Exist")
        return Response("UserName Already Exist")
    
    user = dict(username=customer.get('username'), 
                phone_number=customer.get('phonenumber'), 
                password=make_password(customer.get('password1')), 
                email=customer.get('email'),
                name=customer.get('name'))
    
    serializer = CustomerSerializer(data=user)
    
    if not serializer.is_valid():
        logger.warning("Missing Fields while Registering..")
        serializers.ValidationError("Missing Fields while Registering..")

    try:
        serializer.save()
        logger.info("New Customer Created")
    except AssertionError:
        logger.warning("Data given for Registerion is Invalid")
        return Response("Data given for Registerion is Invalid")
    return Response("New Customer Created")
            
    
@api_view(['POST'])
def login(request):
    """
    Check whether Account is present and allows user to login.

    Parameters:
    Request

    Returns:
    Customer-Id as Response.
    """

    customer = request.data
    
    if not customer:
        logger.info("No Data to Login")
        return Response("No Data to Login")

    try:
        customer_data = Customer.objects.get(username = customer.get("username"))
        if check_password(customer.get('password'), customer_data.password):
            id = customer_data.id
    
    except Customer.DoesNotExist:
        logger.warning("Username or Password Incorrect")
        return Response("Username or Password Incorrect")
    return Response(id)


