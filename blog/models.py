from django.db import models

# Create your models here.
class Articulo (models.Model):
    titulo=models.CharField(max_length=50)
    resumen=models.TextField(max_length=150)
    contenido=models.TextField()
    imagen=models.ImageField()
    autor=models.CharField(max_length=50)

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"


class Contacto (models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    mensaje=models.TextField()
