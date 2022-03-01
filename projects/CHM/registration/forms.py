from django import forms

from employee.models import Employee


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ['created_at', 'updated_at']
