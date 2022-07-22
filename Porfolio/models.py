from django.db import models

class Contactos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"|Nombre: {self.nombre} | Apellido: {self.apellido} | E-Mail: {self.email} | Profesión: {self.profesion} |"

class Certificaciones(models.Model):
    nombre= models.CharField(max_length=30)
    tecnologia= models.CharField(max_length=30)
    emisor= models.CharField(max_length=30)
    fecha= models.DateField()

    def __str__(self):
        return f"|Nombre: {self.nombre} | Tecnologia: {self.tecnologia} | Emisor: {self.emisor} | Fecha: {self.fecha} |"























#######POST################
# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Nombre")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#     class Meta:
#         verbose_name = "categoría"
#         verbose_name_plural = "categorías"
#         ordering = ['-created']

#     def __str__(self):
#         return self.name


# class Post(models.Model):
#     title = models.CharField(max_length=200, verbose_name="Título")
#     content = models.TextField(verbose_name="Contenido")
#     published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
#     image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
#     author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

#     class Meta:
#         verbose_name = "entrada"
#         verbose_name_plural = "entradas"
#         ordering = ['-created']

#     def __str__(self):
#         return self.title

#######POST################
