from django import forms  

from shows.models import Show, ShowCategory
  

class ShowForm(forms.ModelForm):  
    class Meta:  
        model = Show
        exclude = ['created_at', 'updated_at']


class ShowCategoryForm(forms.ModelForm):
    class Meta:  
        model = ShowCategory
        exclude = ['created_at', 'updated_at']