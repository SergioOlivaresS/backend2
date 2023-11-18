from django.contrib import admin
from django.urls import path
from alumno import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indice, name='indice'), 
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('editar_alumno/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('eliminar_alumno/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
]