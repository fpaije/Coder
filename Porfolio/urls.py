from django.urls import path
from Porfolio import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', views.inicio, name='Inicio'),
    path('buscar/', views.buscar),
    path('formacion_academica', views.formacion_academica, name='Formacion_Academica'),
    path('desarrollo_profesional', views.desarrollo_profesional, name='Desarrollo_Profesional'),
    path('agenda_formulario', views.agenda_formulario, name='Agenda_Formulario'),
    path('agregar_certificacion', views.agregar_certificacion, name='Agregar_Certificacion'), #cree esta url para separar de desarrollo profesional
    path('ver_cert', views.ver_cert, name='Ver_Cert'),
    path('eliminar_cert/<certificado_nombre>/', views.eliminar_cert, name='Eliminar_Cert'),
    path('editar_cert/<certificado_nombre>/', views.editar_cert, name='Editar_Cert'),

    #basado en vistas para contactos

    path('contactos/list', views.Contactos_list.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.Contactos_detalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.Contactos_creacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.Contactos_update.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.Contactos_delete.as_view(), name='Delete'),
]