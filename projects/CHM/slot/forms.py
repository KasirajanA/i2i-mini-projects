from django import forms
  
from slot.models import Slot  
  
class SlotForm(forms.ModelForm):
    """
    Generetes a form model for slot nodel 
    """

    class Meta:  
        model = Slot 
        exclude = ['created_at', 'updated_at']