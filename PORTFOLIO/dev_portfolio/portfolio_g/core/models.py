from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100, default='Nome')
    comentario = models.CharField(max_length=500, default="Comentario")
    
    class Meta:
        db_table = 'usuarios'
        verbose_name_plural = 'usuarios'
    
    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.comentario