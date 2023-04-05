from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from usuarios.forms import UserRegisterForm


# Create your views here.

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user is not None:
                login(request, user)

                return redirect("home")

            else:
                return redirect("loginerror")

    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context=context)

def loginerror(request):
    return render(request, 'loginerror.html')

def registro(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home")
        else:
            return render(request, "loginerror.html")
    # form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "registro.html", context=context)
