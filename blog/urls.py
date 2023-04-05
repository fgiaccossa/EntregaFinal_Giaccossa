from django.urls import path, include
import blog.views


urlpatterns = [

    path('', blog.views.Inicio, name="inicio"),
    path('home/', blog.views.Inicio, name="home"),
    path('pages/', blog.views.articulo, name="blog"),
    path('contacto/', blog.views.Contacto, name="contacto"),
    path('about/', blog.views.Nosotros, name="nosotros"),

]