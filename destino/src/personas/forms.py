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

  def clean_nombres(self, *args, **kwargs):
    print('paso')
    name = self.cleaned_data.get('nombre')
    if name.istitle():
      return name
    else:
      raise forms.ValidationError('La primera letra debe estar en mayúsculas')

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