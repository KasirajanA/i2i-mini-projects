from django.urls import path

from registration.views import employee_login, employee_registration

urlpatterns = [
    path('login2', employee_login),
    path('register2', employee_registration)
]