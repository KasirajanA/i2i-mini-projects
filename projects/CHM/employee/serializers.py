from rest_framework import serializers

from employee.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['created_at', 'updated_at']