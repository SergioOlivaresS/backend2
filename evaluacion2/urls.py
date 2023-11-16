from django.contrib import admin
from django.urls import path
from alumno import views
from formularioProfesor import views as profesor_views
from formularioRamos import views as ramos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.indice, name='indice'), 
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('editar_alumno/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('eliminar_alumno/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('formularioramos/', ramos_views.formulario_ramos, name='formularioramos'),
    path('', ramos_views.home, name='home'),
    # Path de ramos
    path('ramos/', ramos_views.ramosData, name='ramosData'),
    path('eliminar_ramo/<int:idRamo>/', ramos_views.eliminar_ramo, name='eliminar_ramo'),
    path('modificar_ramo/<int:idRamo>/', ramos_views.modificar_ramos, name='modificar_ramo'),
    # Path de profesores
    path('formularioprofesor/', profesor_views.formulario_profesor, name='formulario_profesor'),
    path('profesor/', profesor_views.profesorData, name='profesorData'),
    path('eliminar_profesor/<int:idProfesor>/', profesor_views.eliminar_profesor, name='eliminar_profesor'),
    path('modificar_profesor/<int:idProfesor>/', profesor_views.modificar_profesor, name='modificar_profesor'),
    
]