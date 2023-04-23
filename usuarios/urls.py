from django.urls import path
import usuarios.views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signin/', usuarios.views.login_usuario, name="signin"),
    path('loginsuccess/', usuarios.views.loginsuccess, name="loginsuccess"),
    path('loginerror/', usuarios.views.loginerror, name="loginerror"),
    path('signup/', usuarios.views.registro, name="signup"),
    path('signupsuccess/', usuarios.views.signupsuccess, name='signupsuccess'),
    path('signuperror/', usuarios.views.signuperror, name='signuperror'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('perfil/', usuarios.views.perfil, name='perfil'),
    path('editarusuario/', usuarios.views.editarusuario, name='editarusuario'),
    path('eliminarusuario/', usuarios.views.eliminarusuario, name='eliminarusuario'),
]
