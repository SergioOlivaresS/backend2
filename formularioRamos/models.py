from django.db import models
from formularioProfesor.models import Profesor

class Ramos(models.Model):
    idRamo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    carrera = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    creditos = models.IntegerField()
    horas = models.IntegerField()
    sala = models.CharField(max_length=10)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True, related_name='ramos')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ramos'
