# Coder

Buenas Facu, tengo 2 temas de consulta

-1-

![image](https://user-images.githubusercontent.com/56512168/180457600-8b4d3b42-140a-45e3-a79f-097c1cca2c25.png)

- En el botton Certificaciones tengo una lectura con este metodo

def ver_cert(request):

      certificacion = Certificaciones.objects.all() #trae todos los profesores

      contexto= {"certificacion":certificacion} 

      return render(request, 'porfolio/ver_cert.html',contexto)
- Cuando hago click en agregar otra certificacion, deberia direccionarme a "desarrollo profesional" que lo hace correctamente, PERO, no me muestra el formulario, y no estoy pudiendo entender el pq!
El tema es que si ahora quiero seguir con eliminar y demas, voy a tener el mismo problema.

Intente seguir el modelo de las clases, pero no se que esta pasando. 

-2-
Estoy intentando terminar la modificacion de datos (contactos) basado en Vistas de clases. Pero tengo un problema que no estoy aun encontrando el root.

link--
http://127.0.0.1:8000/Porfolio/contactos/list

Puedo ver/listar pero al intentar borrar editar o crear bajo esta modalidad, por alguna razon no esta funcionando, si no es demasiado y me podes decir si vez el problema, seria genial!

Sigo codeando a ver si lo encuentro...si lo encuentro te aviso!, gracias!





