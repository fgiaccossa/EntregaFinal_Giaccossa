from django.urls import path, include
import blog.views


urlpatterns = [

    path('', blog.views.inicio, name="inicio"),
    path('home/', blog.views.inicio, name="home"),
    path('pages/', blog.views.publicaciones, name="publicaciones"),
    path('publicar/', blog.views.articulo, name="blog"),
    path('blogsuccess/', blog.views.blogsuccess, name="blogsuccess"),
    path('blogerror/', blog.views.blogerror, name="blogerror"),
    path('leerarticulo/', blog.views.leerarticulo, name="leerarticulos"),
    path('contacto/', blog.views.contacto, name="contacto"),
    path('contactoerror/', blog.views.contactoerror, name="contactoerror"),
    path('about/', blog.views.nosotros, name="nosotros"),

]