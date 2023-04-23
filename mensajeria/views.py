from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mensajeria.models import Conversacion, Mensaje
from mensajeria.forms import NuevaConversacionForm, NuevoMensajeForm


@login_required
def lista_conversaciones(request):
    conversaciones = request.user.conversaciones.all()
    return render(request, 'conversaciones.html', {'conversaciones': conversaciones})

@login_required
def ver_conversacion(request, conversacion_id):
    conversacion = get_object_or_404(request.user.conversaciones, id=conversacion_id)
    mensajes = conversacion.mensajes.all()
    if request.method == 'POST':
        texto = request.POST['texto']
        mensaje = Mensaje(conversacion=conversacion, autor=request.user, texto=texto)
        mensaje.save()
        return redirect('ver_conversacion', conversacion_id=conversacion.id)
    return render(request, 'ver_conversacion.html', {'conversacion': conversacion.asunto, 'mensajes': mensajes})

@login_required()
def eliminarconversacion(request, conversacion_id):
    conversacion = Conversacion.objects.get(id=conversacion_id)
    conversacion.delete()
    return render(request, "eliminarconversacion.html")


@login_required
def nueva_conversacion(request, asunto=None):
    if request.method == 'POST':
        form = NuevaConversacionForm(request.POST)
        if form.is_valid():
            conversacion = form.save(creador=request.user, asunto=form.cleaned_data['asunto'])
            return redirect('mensajenuevo', conversacion_id=conversacion.id)
    else:
        form = NuevaConversacionForm()
    return render(request, 'nueva_conversacion.html', {'form': form})

@login_required
def nuevo_mensaje(request, conversacion_id):
    conversacion = Conversacion.objects.get(id=conversacion_id)
    if request.method == 'POST':
        form = NuevoMensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.conversacion = conversacion
            mensaje.autor_id = request.user.id
            mensaje.save()
            return redirect('ver_conversacion', conversacion_id=conversacion_id)
    else:
        form = NuevoMensajeForm()
    return render(request, 'mensajenuevo.html', {'form': form, 'conversacion': conversacion})