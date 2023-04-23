from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Conversacion(models.Model):
    usuarios = models.ManyToManyField(User, related_name='conversaciones')
    asunto = models.CharField(max_length=50)

    def __str__(self):
        return f"Asunto: {self.asunto}"

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, related_name='mensajes')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=50)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Autor: {self.autor}", f"Asunto: {self.asunto}", f"Fecha: {self.fecha_creacion}"
