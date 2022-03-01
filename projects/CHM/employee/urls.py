from django.urls import path

from employee.views import fetch_employees, remove_employee


urlpatterns = [
    path('fetchemployees', fetch_employees),
    path('removeemployee/<int:id>', remove_employee)
]