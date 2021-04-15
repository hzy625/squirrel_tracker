from .models import *
from django import forms

class SquirrelForm(forms.ModelForm):
    """
    form
    """
    class Meta:
        model = Squirrel
        fields = '__all__'

class SquirrelUpdateForm(forms.ModelForm):
    """
    update form
    """
    class Meta:
        model = Squirrel
        fields = ('unique_squirrel_id', 'latitude', 'longitude', 'shift', 'date', 'age')

