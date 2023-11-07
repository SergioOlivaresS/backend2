from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno/lista_alumnos.html', {'alumnos': alumnos})

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumno/crear_alumno.html', {'form': form})

def editar_alumno(request, id):
    alumno = Alumno.objects.get(pk=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumno/editar_alumno.html', {'form': form})

def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(pk=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('lista_alumnos')
    return render(request, 'alumno/eliminar_alumno.html', {'alumno': alumno})