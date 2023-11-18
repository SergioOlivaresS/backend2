from django.shortcuts import render, redirect
from .forms import ProfesorForm 
from .models import Profesor

# Create your views here.
def home(request):
    return render(request, "index/home.html")

def profesorData(request):
    profesores = Profesor.objects.all()
    data = {'profesores': profesores}  # Cambié 'profesor' a 'profesores'
    return render(request, 'formularioprofesor/profesor.html', data)

def formulario_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesorData')
    else:
        form = ProfesorForm()

    return render(request, 'formularioprofesor/formularioprofesor.html', {'form': form})

def eliminar_profesor(request, idProfesor):
    profesor = Profesor.objects.get(id=idProfesor)
    profesor.delete()
    return redirect('profesorData')

def modificar_profesor(request, idProfesor):
    profesor = Profesor.objects.get(id=idProfesor)
    form = ProfesorForm(instance=profesor)

    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('profesorData')

    data = {'form': form, 'modo': 'modificar', 'idProfesor': idProfesor}
    return render(request, 'formularioprofesor/formularioprofesormod.html', data)