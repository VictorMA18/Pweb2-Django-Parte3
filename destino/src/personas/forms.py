from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
  class Meta:
    model = Persona
    fields = [
        'nombre',
        'apellidos',
        'edad',
        'donador',
    ]

class RawPersonaForm(forms.Form):
  nombre = forms.CharField(
    widget= forms.Textarea(
      attrs={
        'placeholder': 'Solo tu nombre, porfavor',
        'id' : 'nombreID',
        'class': 'scpecial',
        'cols': '10',
      }
    )
  )
  apellidos = forms.CharField()
  edad = forms.IntegerField()
  donador = forms.BooleanField()