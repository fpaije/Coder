from django.urls import path
from Porfolio import views


urlpatterns = [
   
    path('', views.inicio, name='Inicio'),
    path('buscar/', views.buscar),
    path('formacion_academica', views.formacion_academica, name='Formacion_Academica'),
    path('desarrollo_profesional', views.desarrollo_profesional, name='Desarrollo_Profesional'),
    path('agenda_formulario', views.agenda_formulario, name='Agenda_Formulario'),
    path('agregar_certificacion', views.agregar_certificacion, name='Desarrollo_Profesional'),
    path('ver_cert', views.ver_cert, name='Ver_Cert'),
    path('eliminar_cert/<certificado_nombre>/', views.eliminar_cert, name='Eliminar_Cert'),
    path('editar_cert/<certificado_nombre>/', views.editar_cert, name='Editar_Cert'),
]