from django import forms  

from conferencehall.models import ConfernceHall 

  
class ConferenceHallForm(forms.ModelForm):
    """
    Generetes a form model for conference hall nodel 
    """ 

    class Meta:  
        model = ConfernceHall 
        exclude = ['created_at', 'updated_at']