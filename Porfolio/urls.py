from django.urls import path
from Porfolio import views
# from . import views
# from .views import *

urlpatterns = [
   
    path('', views.inicio, name='Inicio'), #name puede ser cualquiera
#   path('cursos', views.cursos, name="Cursos") #herencia test
    path('formacion_academica', views.formacion_academica, name='Formacion_Academica'),
    path('desarrollo_profesional', views.desarrollo_profesional, name='Desarrollo_Profesional'),
    path('agenda_formulario', views.agenda_formulario, name='Agenda_Formulario'),
    path('agregar_certificacion', views.agregar_certificacion, name='Desarrollo_Profesional'),
    path('buscar/', views.buscar), #Vista Busqueda
    path('ver_cert', views.ver_cert, name='Ver_Cert'),# Vista Certificaciones
    path('eliminar_cert/<certificado_nombre>/', views.eliminar_cert, name="Eliminar_Cert"),
    # path('blog', views.blog, name='Blog'),
    # path('category/<int:category_id>/', views.category, name='Category'),
]