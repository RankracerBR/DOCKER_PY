from django.db import models

# Create your models here.

class Email(models.Model):
    def __init__(self, nome, email,comentario):
        nome = models.CharField(max_length=100, default="Nome")
        email = models.CharField(max_length=100, default="Email")
        comentario = models.CharField(max_length=900, default="Email")
        
        def __str__(self):
            return self.nome
        
        def __str__(self):
            return self.email
        
        def __str__(self):
            return self.comentario