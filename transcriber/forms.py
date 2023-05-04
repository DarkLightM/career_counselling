from django import forms
from .models import *


class AddFileForm(forms.ModelForm):
    class Meta:
        model = Transcriber
        fields = ['name', 'audio_source', 'slug', 'profile']
