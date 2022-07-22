# Coder

![image](https://user-images.githubusercontent.com/56512168/180457600-8b4d3b42-140a-45e3-a79f-097c1cca2c25.png)

- En el botton Certificaciones tengo una lectura con este metodo

def ver_cert(request):

      certificacion = Certificaciones.objects.all() #trae todos los profesores

      contexto= {"certificacion":certificacion} 

      return render(request, 'porfolio/ver_cert.html',contexto)
- Cuando hago click en agregar otra certificacion, deberia direccionarme a "desarrollo profesional" que lo hace correctamente, PERO, no me muestra el formulario, y no estoy pudiendo entender el pq!
El tema es que si ahora quiero seguir con eliminar y demas, voy a tener el mismo problema.

Intente seguir el modelo de las clases, pero no se que esta pasando. 


####
Tampoco estoy pudiendo encontrar el problema con el metodo de edicion, logre configurar todo, pero cuando haces una edicion y le das a enviar se rompe con este error

"AttributeError: 'Certificacion_formulario' object has no attribute 'cleaned_data'"

HELP :)


