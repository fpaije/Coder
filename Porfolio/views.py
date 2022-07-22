from django.shortcuts import render
from django.http import HttpResponse
from Porfolio.forms import Certificacion_formulario, Contactos_formulario
from Porfolio.models import Certificaciones, Contactos #respuesta Http
# from .models import Post, Category #BLOG
# from django.shortcuts import render, get_object_or_404#BLOG


def inicio(request): # http://127.0.0.1:8000/Porfolio/

      return render(request, 'porfolio/inicio.html') #nombre de carpeta/nombreHTML

# def cursos(request): #http://127.0.0.1:8000/Porfolio/cursos

#       return render(request, "porfolio/cursos.html")

def formacion_academica(request): # http://127.0.0.1:8000/Porfolio/

      return render(request, 'porfolio/formacion_academica.html')

def desarrollo_profesional(request): # http://127.0.0.1:8000/Porfolio/

      return render(request, 'porfolio/desarrollo_profesional.html')

# Metodo Formulario

# def agenda_formulario(request):

#       if request.method == 'POST':
#             agenda = Contactos(request.POST['nombre'], request.POST['apellido'], request.POST['email'], request.POST['profesion'])
#             agenda.save()
      
#             return render(request, 'porfolio/inicio.html')
#       return render(request, 'porfolio/agenda_formulario.html')

#### METODO PARA AGREGAR CONTACTOS A LA DB -- START#####
def agenda_formulario(request):

      if request.method == 'POST':

            miagenda = Contactos_formulario(request.POST)  #aquí mellega toda la información del html

            if miagenda.is_valid():   #Si pasó la validación de Django

                  informacion = miagenda.cleaned_data

                  agenda = Contactos(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
                  agenda.save()
                  
                  return render(request, 'porfolio/inicio.html')

      else:

            miagenda = Contactos_formulario()
      
      return render(request, 'porfolio/agenda_formulario.html', {'miagenda':miagenda})
####  END #####

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


#### METODO PARA AGREGAR CERTIFICACIONES -- START#####
def agregar_certificacion(request):

      if request.method == 'POST':

            micertificacion = Certificacion_formulario(request.POST)  #aquí mellega toda la información del html

            if micertificacion.is_valid():   #Si pasó la validación de Django

                  informacion = micertificacion.cleaned_data

                  cert = Certificaciones(nombre=informacion['nombre'], tecnologia=informacion['tecnologia'], emisor=informacion['emisor'], fecha=informacion['fecha'])
                  cert.save()
                  
                  return render(request, 'porfolio/inicio.html')

      else:

            micertificacion = Certificacion_formulario()
      
      return render(request, 'porfolio/desarrollo_profesional.html', {'micertificacion':micertificacion})
####  END #####

########### METODO VER CERTIFICACIONES -- START#####
def ver_cert(request):

      certificacion = Certificaciones.objects.all() #trae todos los profesores

      contexto= {"certificacion":certificacion} 

      return render(request, 'porfolio/ver_cert.html',contexto)

########### METODO VER CERTIFICACIONES -- START#####
####  END #####

########### METODO ELIMINAR CERTIFICACIONES -- START#####
def eliminar_cert(request, certificado_nombre):

      certificacion = Certificaciones.objects.get(nombre=certificado_nombre)
      certificacion.delete()
      
      #vuelvo al menú
      certs = Certificaciones.objects.all() #trae todos los profesores

      contexto= {"certs":certs} 

      return render(request, "porfolio/desarrollo_profesional.html",contexto)


########### METODO VER CERTIFICACIONES -- START#####




# def blog(request):
#     posts = Post.objects.all()
#     return render(request, 'porfolio/blog.html', {'posts':posts})

# def category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     return render(request, 'porfolio/category.html', {'category':category})


