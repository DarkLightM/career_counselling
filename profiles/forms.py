from django import forms
from .models import *


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['surname', 'name', 'second_name', 'age', 'telephone_number', 'email', 'profile', 'slug']


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'slug']
