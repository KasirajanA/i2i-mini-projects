from django.urls import path

from registration.views import employee_login, employee_registration

urlpatterns = [
    path('login', employee_login),
    path('register', employee_registration)
]