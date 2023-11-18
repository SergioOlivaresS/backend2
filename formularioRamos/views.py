from django.shortcuts import render
from django.http import HttpResponse
from formularioRamos.models import Ramos
from django.shortcuts import redirect
from .forms import RamosForm 

# Create your views here.

def home(request):
    return render(request, "index/home.html")


def renderTemplate(request):
   return render(request, "formularioRamos/formularioRamos.html")

def ramosData (request):
    ramos = Ramos.objects.all ()
    data = {'ramos' : ramos}
    return render (request, 'ramos/ramos.html', data)

def formulario_ramos(request):
    if request.method == 'POST':
        form = RamosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ramosData')
    else:
        form = RamosForm()

    return render(request, 'formularioramos/formularioramos.html', {'form': form})

def eliminar_ramo(request, idRamo):
    ramo = Ramos.objects.get(idRamo = idRamo)
    ramo.delete()
    return redirect('/ramos')

def modificar_ramos(request, idRamo):
    ramo = Ramos.objects.get(idRamo=idRamo)
    form = RamosForm(instance=ramo)

    if request.method == 'POST':
        form = RamosForm(request.POST, instance=ramo)
        if form.is_valid():
            form.save()
            return redirect('ramosData')

    data = {'form': form, 'modo': 'modificar', 'idRamo': idRamo}
    return render(request, 'formularioramos/formularioramosmod.html', data)

