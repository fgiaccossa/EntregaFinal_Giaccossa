from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import ArticuloForm, ContactoForm
from blog.models import Articulo


# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def publicaciones(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos": articulos}
    return render(request, "publicaciones.html", contexto)
    #return render (request, 'publicaciones.html')
@login_required
def articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return render(request, "blogsuccess.html")
        else:
            return render(request, "blogerror.html")

    form = ArticuloForm()

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
            return render(request, "errorenvio.html")
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
    contexto={'articulo':articulo}
    return render(request, 'articulo.html', contexto)

def editararticulo(request, pk):
    get_articulo = Articulo.objects.get(id=pk)

    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return render(request, "blogsuccess.html")
        else:
            return render(request, "blogerror.html")

    #form = ArticuloForm()
    get_articulo = Articulo.objects.get(id=pk)

    context = {
        "form": ArticuloForm(initial={"titulo":get_articulo.titulo, "resumen":get_articulo.resumen, "contenido":get_articulo.contenido, "imagen":get_articulo.imagen, "autor":get_articulo.autor})

    }
    return render(request, 'blog.html', context=context)