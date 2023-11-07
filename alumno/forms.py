import re
from typing import Any
from django import forms
from .models import Alumno
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
           'fechaDeNacimiento': forms.TextInput(attrs={'type': 'date', 'pattern': r'\d{2}/\d{2}/\d{4}', 'placeholder': 'dd/mm/yyyy'}),
        }
        


   
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if rut:
            rut = re.sub(r'\.', '', rut).upper()
            if not re.match(r'^\d{1,8}-[0-9K]$', rut):
                raise forms.ValidationError('El RUT no es válido.')
        return rut

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
    
    def clean_carrera(self):
        carrera = self.cleaned_data['carrera']
        if len(carrera) < 6:
            raise forms.ValidationError('La carrera debe tener almenos 6 letras.')
        return carrera


    def clean_fechaDeNacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fechaDeNacimiento')
        if fecha_nacimiento:
            edad_minima = timezone.now().date() - timedelta(days=365 * 18)  
            if fecha_nacimiento > edad_minima:
                raise ValidationError('El alumno debe ser mayor de 18 años.')
        return fecha_nacimiento
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and email.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return email