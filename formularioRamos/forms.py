from django import forms
from formularioRamos.models import Ramos , Profesor
from typing import Any
from django import forms

class RamosForm(forms.ModelForm):
    profesor = forms.ModelChoiceField(
        queryset=Profesor.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Ramos
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'sala': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 2:
            raise forms.ValidationError('El nombre debe tener almenos 2 letras.')
        return nombre
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripcion debe ser mas larga.')
        return descripcion
    
    def clean_carrera(self):
        carrera = self.cleaned_data['carrera']
        if len(carrera) < 6:
            raise forms.ValidationError('La carrera debe tener almenos 6 letras.')
        return carrera

    def clean_creditos(self):
        creditos = self.cleaned_data['creditos']
        if creditos <= 0:
            raise forms.ValidationError('Los créditos deben ser un número positivo.')
        return creditos
    
    def clean_horas(self):
        horas = self.cleaned_data['horas']
        if horas <= 0:
            raise forms.ValidationError('Las horas deben ser un número positivo.')
        return horas
    
    def clean_sala(self):
        sala = self.cleaned_data['sala']
        if len(sala) > 5:
            raise forms.ValidationError('La sala no puede tener más de 5 letras.')
        return sala
