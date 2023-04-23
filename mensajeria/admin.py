from django.contrib import admin

from mensajeria.models import Conversacion, Mensaje

# Register your models here.
admin.site.register(Mensaje)
admin.site.register(Conversacion)