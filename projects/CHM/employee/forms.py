from django import forms  

from employee.models import Employee 

  
class EmployeeForm(forms.ModelForm):
    """
    Generetes a form model for conference hall nodel 
    """ 

    class Meta:  
        model = Employee
        exclude = ['created_at', 'updated_at']