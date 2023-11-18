from django.db import models
from formularioRamos.models import Ramos

class Alumno(models.Model):
    idalumno = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    carrera = models.CharField(max_length=60)
    fechaDeNacimiento = models.DateField()
    email = models.EmailField()
    ramos = models.ManyToManyField(Ramos, related_name='alumnos')  


    def get_ramos_display(self):
        return ', '.join([str(ramo) for ramo in self.ramos.all()])
    get_ramos_display.short_description = 'Ramos'

    def __str__(self):
        return f" ID {self.idalumno} | Rut {self.rut} | {self.nombre} {self.apellido} | {self.fechaDeNacimiento} | {self.carrera} | {self.email} |"