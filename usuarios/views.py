from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user
from usuarios.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])

            if user is not None:
                login(request, user)

                return redirect("loginsuccess")

            else:
                return redirect("loginerror")

    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context=context)


def loginsuccess(request):
    return render(request, 'loginsuccess.html')

def loginerror(request):
    return render(request, 'loginerror.html')

def registro(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, "registrosuccess.html")
        else:
            return render(request, "registroerror.html")
    # form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "registro.html", context=context)

def signupsuccess(request):
    return render(request, 'registrosuccess.html')

def signuperror(request):
    return render(request, 'registroerror.html')

def editarusuario(request):

    user = request.user

    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            informacion = form.cleaned_data

            user.username = informacion["username"]
            user.email = informacion["email"]
            user.is_staff = informacion["is_staff"]

            #try:
            #    user.avatar.imagen = informacion["imagen"]
            #except:
            #    avatar = Avatar(user=user, imagen=informacion["imagen"])
            #    avatar.save()

            user.save()
            return render(request, "edicionsuccess.html")
        else:
            return render(request, "contactoerror.html")

    form = UserRegisterForm(initial={
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff
    })

    context = {
        "form": form,
    }

    return render(request, "registro.html", context=context)

@login_required
def eliminarusuario(request):
    user = request.user
    user.delete()
    return render(request, "eliminarusuario.html")

@login_required
def perfil(request):
    return render(request, "perfil.html")