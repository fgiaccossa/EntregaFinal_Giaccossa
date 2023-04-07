from django import forms
from django.contrib.auth.models import User
from blog.models import Articulo, Contacto
from django.conf import settings
from django.contrib.auth import get_user_model

class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    resumen = forms.CharField(widget=forms.Textarea, max_length=150)
    contenido = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()
    autor = forms.CharField(max_length=50)

    def save(self):
        information = self.cleaned_data
        articulo = Articulo(
            titulo=information["titulo"],
            resumen=information["resumen"],
            contenido=information["contenido"],
            imagen=information["imagen"],
            autor = information["autor"],
        )
        articulo.save()
        return articulo


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)


    def save(self):
        information = self.cleaned_data
        contacto = Contacto(
            nombre=information["nombre"],
            email=information["email"],
            mensaje=information["mensaje"],
        )
        contacto.save()
        return contacto
