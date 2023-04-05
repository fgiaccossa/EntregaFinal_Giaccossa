from django.shortcuts import render, redirect

from blog.forms import ArticuloForm, ContactoForm


# Create your views here.

def Inicio(request):
    return render(request, 'index.html')


def articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("blog")
        else:
            return render(request, "blogerror.html")

    form = ArticuloForm()

    context = {
        "form": form
    }
    return render(request, 'blog.html', context=context)


def Nosotros(request):
    return render(request, 'nosotros.html')


def Contacto(request):
    if request.method == "POST":

        form = Contacto(request.POST)

        if form.is_valid():
            form.save()

            return redirect("blog")
        else:
            return render(request, "errorenvio.html")
    form = Contacto()

    context = {
        "form": form
    }
    return render(request, 'contacto.html', context=context)
