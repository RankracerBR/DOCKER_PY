from django.contrib import admin
from .models import Usuarios

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nome','comentario')
    list_filter = ('nome',)

admin.site.register(Usuarios,UsuariosAdmin)