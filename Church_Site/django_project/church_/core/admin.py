from django.contrib import admin
from .models import Email
# Register your models here.

class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('nome','sobrenome')


admin.site.register(Email)