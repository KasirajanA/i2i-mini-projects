from django import forms 

from movies.models import Movie

  
class MovieForm(forms.ModelForm):  
    class Meta:  
        model = Movie
        exclude = ['created_at', 'updated_at']

