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
    nuevas_ramos = models.ManyToManyField(Ramos, through='Inscripcion', related_name='alumnos_nuevos')

    def get_ramos_display(self):
        return ', '.join([str(inscripcion.ramo) for inscripcion in self.inscripcion_set.all()])

    get_ramos_display.short_description = 'Ramos'

    def __str__(self):
        return f" ID {self.idalumno} | Rut {self.rut} | {self.nombre} {self.apellido} | {self.fechaDeNacimiento} | {self.carrera} | {self.email} |"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    ramo = models.ForeignKey(Ramos, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inscribir"

    def __str__(self):
        return f"{str(self.alumno)} inscrito en {str(self.ramo)}"
