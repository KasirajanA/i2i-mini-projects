from django import forms  

from theatres.models import Theatre
  

class TheatreForm(forms.ModelForm):  
    class Meta:  
        model = Theatre
        exclude = ['created_at', 'updated_at']