from django.shortcuts import render, redirect

from blog.forms import ArticuloForm, ContactoForm


# Create your views here.

def inicio(request):
    return render(request, 'index.html')


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
