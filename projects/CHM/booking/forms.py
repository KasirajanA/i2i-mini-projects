from django import forms

from booking.models import Booking  
 
  
class BookingForm(forms.ModelForm):
    """
    Generetes a form model for Booking nodel 
    """ 

    class Meta:  
        model = Booking 
        exclude = ['created_at', 'updated_at']