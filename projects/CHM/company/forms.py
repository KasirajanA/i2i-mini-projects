from django import forms
  
from company.models import Company  
  
class CompanyForm(forms.ModelForm):
    """
    Generetes a form model for company nodel 
    """

    class Meta:  
        model = Company 
        exclude = ['created_at', 'updated_at']