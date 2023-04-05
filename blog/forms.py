from django import forms

from blog.models import Articulo


class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    resumen= forms.CharField(max_length=150)
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
            autor=information["autor"],
        )
        articulo.save()
        return articulo

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.Textarea()
