from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from dataclasses import fields


class Contactos_formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)


class Certificacion_formulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    tecnologia= forms.CharField(max_length=30)
    emisor= forms.CharField(max_length=30)
    fecha= forms.DateField()
