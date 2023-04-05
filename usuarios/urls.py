from django.urls import path
import usuarios.views

urlpatterns = [
    path('signin/', usuarios.views.login_usuario, name="signin"),
    path('loginerror/', usuarios.views.loginerror, name="loginerror"),
    path('signup/', usuarios.views.registro, name="signup")
]