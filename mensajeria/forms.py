from .models import Conversacion
from .models import Mensaje
from django import forms
from django.contrib.auth.models import User
class NuevaConversacionForm(forms.Form):
    asunto = forms.CharField(max_length=50)
    usuarios = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)


    def save(self, creador, asunto):
        conversacion = Conversacion(asunto=asunto)
        conversacion.save()
        conversacion.usuarios.add(creador)
        for usuario in self.cleaned_data['usuarios']:
            conversacion.usuarios.add(usuario)

        return conversacion


class NuevoMensajeForm(forms.ModelForm):
      class Meta:
        model = Mensaje
        fields = ['texto']
