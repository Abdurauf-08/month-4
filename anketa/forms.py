from django import forms
from . import models

class AnketaForm(forms.ModelForm):
    class Meta:
        model = models.Anketa
        fields = "__all__"
        
