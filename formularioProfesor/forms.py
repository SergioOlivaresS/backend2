from django import forms
from .models import Profesor
import re
from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {
            'RUT': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Area': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_rut(self):
        RUT = self.cleaned_data.get('RUT')
        if RUT:
            RUT = re.sub(r'\.', '', RUT).upper()
            if not re.match(r'^\d{1,8}-[0-9K]$', RUT):
                raise forms.ValidationError('El RUT no es válido.')
        return RUT

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 2:
            raise forms.ValidationError('El nombre debe tener almenos 2 letras.')
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if len(apellido) < 2:
            raise forms.ValidationError('El apellido debe tener almenos 2 letras.')
        return apellido
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        telefonostr = str(telefono)
        if len(telefonostr) < 9:
            raise forms.ValidationError('El telefono debe tener 9 numeros.')
        return telefono

