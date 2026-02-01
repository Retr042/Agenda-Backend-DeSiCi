from django.contrib import admin
from .models import Contacto, Direccion, Telefono

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Telefono)

