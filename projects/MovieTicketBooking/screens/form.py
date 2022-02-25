from django import forms  

from screens.models import Screen
  

class ScreenForm(forms.ModelForm):  
    class Meta:  
        model = Screen
        exclude = ['created_at', 'updated_at']