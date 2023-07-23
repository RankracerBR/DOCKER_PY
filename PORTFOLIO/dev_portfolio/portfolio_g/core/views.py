from django.shortcuts import render
from datetime import datetime
from core.models import Usuarios
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create your views here.
def main_page(request):
    now = datetime.now()
    hora = now.hour
   
    if hora < 12:
        mensagem = "BOM DIA!"
    elif hora < 18:
        mensagem = "BOA TARDE!"
    else:
        mensagem = "BOA NOITE!"

    return render(request, 'index.html', {"mensagem": mensagem})


def enviar_comentario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        comentario = request.POST.get('comentario')
        usuario = Usuarios(nome=nome, comentario=comentario, data_postagem=datetime.now())
        usuario.save()

    usuarios = Usuarios.objects.all()
    return render(request, 'secao_comentario.html', {'usuarios': usuarios})
