from django.shortcuts import render, HttpResponse

from acceso.utils.decoradores import login_requerido

def index(request):
    return render(request, 'core/index.html')
