from django.urls import path, include
import mensajeria.views
import blog.urls
import usuarios.urls

urlpatterns = [

    path('', blog.views.inicio, name="inicio"),
    path('home/', blog.views.inicio, name="home"),
    path('conversaciones/', mensajeria.views.lista_conversaciones, name="conversaciones"),
    path('nuevaconversacion/', mensajeria.views.nueva_conversacion, name="nuevaconversacion"),
    path('ver_conversacion/<int:conversacion_id>/', mensajeria.views.ver_conversacion, name="ver_conversacion"),
    path('eliminarconversacion/<int:conversacion_id>/', mensajeria.views.eliminarconversacion, name="eliminarconversacion"),
    path('mensajenuevo/<int:conversacion_id>', mensajeria.views.nuevo_mensaje, name="mensajenuevo"),
    #path('mensajenuevo/<int:conversacion_id>', mensajeria.views.nuevo_mensaje, name="mensajenuevo"),
]
