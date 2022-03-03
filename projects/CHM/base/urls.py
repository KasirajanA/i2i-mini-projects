from lib2to3.pytree import Base
from django.urls import path

from base.views import BaseView


urlpatterns = [
    path('', BaseView.home, name='home'),
    path('administrator', BaseView.admin, name='admin'),
    path('employee', BaseView.employee, name='employee')
   
]

 