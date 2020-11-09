from django import forms
from .models import *
  
  
class GeeksForm(forms.ModelForm):
  
    class Meta:
        model = GeeksModel
  
        fields = [
            "title",
            "description",
        ]


class CarsOwnerForm(forms.ModelForm):
  
    class Meta:
        model = User
  
        fields = [
            "first_name",
            "last_name",
            "dob",
            "PassportID",
            "HomeAddress",
            "Nationality",
        ]


class CarForm(forms.ModelForm):
  
    class Meta:
        model = Car
  
        fields = [
            "mark",
            "model",
            "color",
            "state_number",
        ]
