from django.shortcuts import render
from datetime import datetime
from .models import Usuarios

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

def Usuario_Comentario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        comentario = request.POST['comentario']
        usuario = Usuarios(nome=nome, comentario=comentario)
        usuario.save()
        return render('secao_cometario.html')
    return render(request, 'secao_comentario.html')