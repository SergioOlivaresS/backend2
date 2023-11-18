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
            raise forms.ValidationError('El nombre debe tener al menos 2 letras.')
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if len(apellido) < 2:
            raise forms.ValidationError('El apellido debe tener al menos 2 letras.')
        return apellido
    
    def clean_Telefono(self):
        telefono = self.cleaned_data['Telefono']
        telefonostr = str(telefono)
        if len(telefonostr) != 9 or telefono <= 0:
            raise forms.ValidationError('El teléfono debe tener 9 números y ser positivo.')
        return telefono
    
    def clean_Area(self):
        area = self.cleaned_data['Area']
        if len(area) < 4:
            raise forms.ValidationError('El área debe tener al menos 4 letras.')
        return area
    
    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if email and email.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return email