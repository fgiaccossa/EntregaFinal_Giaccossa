from django.urls import path, include
import blog.views


urlpatterns = [

    path('', blog.views.inicio, name="inicio"),
    path('home/', blog.views.inicio, name="home"),
    path('pages/', blog.views.articulo, name="blog"),
    path('blogsuccess/', blog.views.blogsuccess, name="blogsuccess"),
    path('blogerror/', blog.views.blogerror, name="blogerror"),
    path('contacto/', blog.views.contacto, name="contacto"),
    path('contactoerror/', blog.views.contactoerror, name="contactoerror"),
    path('about/', blog.views.nosotros, name="nosotros"),


]