from django import forms  

from seats.models import Seat
  

class SeatForm(forms.ModelForm):  
    class Meta:  
        model = Seat
        exclude = ['created_at', 'updated_at']