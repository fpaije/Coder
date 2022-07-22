from django.shortcuts import render
from django.http import HttpResponse
from Porfolio.forms import Certificacion_formulario, Contactos_formulario
from Porfolio.models import Certificaciones, Contactos 



def inicio(request): 

      return render(request, 'porfolio/inicio.html') 


def formacion_academica(request): 

      return render(request, 'porfolio/formacion_academica.html')

def desarrollo_profesional(request): 

      return render(request, 'porfolio/desarrollo_profesional.html')


#### METODO PARA AGREGAR CONTACTOS A LA DB -- START#####
def agenda_formulario(request):

      if request.method == 'POST':

            miagenda = Contactos_formulario(request.POST) 

            if miagenda.is_valid():   

                  informacion = miagenda.cleaned_data

                  agenda = Contactos(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
                  agenda.save()
                  
                  return render(request, 'porfolio/inicio.html')

      else:

            miagenda = Contactos_formulario()
      
      return render(request, 'porfolio/agenda_formulario.html', {'miagenda':miagenda})
#### METODO PARA AGREGAR CONTACTOS A LA DB -- END#####


#### METODO BUSCAR CONTACTOS A LA DB -- START#####
def buscar(request):

      if request.GET["profesion"]:
	      
            profesion = request.GET['profesion'] 
            contactoss = Contactos.objects.filter(profesion__icontains=profesion)

            return render(request, "porfolio/inicio.html", {"profesion":profesion, "contactoss":contactoss})

      else: 

	      respuesta = "No tengo amigo con esa profesion"

      #No olvidar from django.http import HttpResponse
      return render(request, "porfolio/inicio.html", {"respuesta": respuesta})
#### METODO BUSCAR CONTACTOS A LA DB -- END#####


#### METODO PARA AGREGAR CERTIFICACIONES -- START#####
def agregar_certificacion(request):

      if request.method == 'POST':

            micertificacion = Certificacion_formulario(request.POST)  

            if micertificacion.is_valid():   
                  informacion = micertificacion.cleaned_data

                  cert = Certificaciones(nombre=informacion['nombre'], tecnologia=informacion['tecnologia'], emisor=informacion['emisor'], fecha=informacion['fecha'])
                  cert.save()
                  
                  return render(request, 'porfolio/inicio.html')

      else:

            micertificacion = Certificacion_formulario()
      
      return render(request, 'porfolio/desarrollo_profesional.html', {'micertificacion':micertificacion})
#### METODO PARA AGREGAR CERTIFICACIONES -- END#####


########### METODO VER CERTIFICACIONES -- START#####
def ver_cert(request):

      certificacion = Certificaciones.objects.all() 

      contexto= {"certificacion":certificacion} 

      return render(request, 'porfolio/ver_cert.html',contexto)
########### METODO VER CERTIFICACIONES -- END#####


########### METODO ELIMINAR CERTIFICACIONES -- START#####
def eliminar_cert(request, certificado_nombre):

      certificacion = Certificaciones.objects.get(nombre=certificado_nombre)
      certificacion.delete()
      
      
      certs = Certificaciones.objects.all()

      contexto= {"certs":certs} 

      return render(request, "porfolio/desarrollo_profesional.html",contexto)
########### METODO ELIMINAR CERTIFICACIONES -- END#####





