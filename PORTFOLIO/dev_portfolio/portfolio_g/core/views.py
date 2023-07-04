from django.shortcuts import render
from datetime import datetime

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

