import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import ArticuloForm, ContactoForm
from blog.models import Articulo
from django.contrib.auth.models import User


# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def publicaciones(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos": articulos}
    return render(request, "publicaciones.html", contexto)
    # return render (request, 'publicaciones.html')


@login_required
def articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES, initial={'autor': request.user.username})

        if form.is_valid():
            form.save(user=request.user)
            return render(request, "blogsuccess.html")
        else:
            return render(request, "blogerror.html")
    form = ArticuloForm(initial={'autor': request.user.username})

    context = {
        "form": form
    }

    return render(request, 'blog.html', context=context)


def blogsuccess(request):
    return render(request, 'blogsuccess.html')


def blogerror(request):
    return render(request, 'blogerror.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def contacto(request):
    if request.method == "POST":

        form = ContactoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("home")
        else:
            return render(request, "contactoerror.html")
    form = ContactoForm()

    context = {
        "form": form
    }
    return render(request, 'contacto.html', context=context)


def contactoerror(request):
    return render(request, 'contactoerror.html')


@login_required
def eliminararticulo(request, pk):
    articulo = Articulo.objects.get(id=pk)
    articulo.delete()
    return render(request, "eliminararticulo.html")


def leerarticulo(request, pk):
    articulo = Articulo.objects.get(id=pk)
    contexto = {'articulo': articulo}
    return render(request, 'articulo.html', contexto)


@login_required
def editararticulo(request, pk):
    articulo = Articulo.objects.get(id=pk)

    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)

        if form.is_valid():

            informacion = form.cleaned_data

            articulo.titulo = informacion["titulo"]
            articulo.resumen = informacion["resumen"]
            articulo.contenido = informacion["contenido"]
            articulo.imagen = informacion["imagen"]
            articulo.autor = request.user
            articulo.fecha_creacion = datetime.datetime.now()

            articulo.save()
            return redirect("publicaciones")
        else:
            return render(request, 'blogediterror.html')

    form = ArticuloForm(instance=articulo)


    context = {
        "form": form,
        "titulo": "Editar publicaccion",
        "enviar": "Editar",
    }

    return render(request, "blog.html", context=context)
