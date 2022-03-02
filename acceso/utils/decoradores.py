
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def login_requerido(function):
    def wrap(request, *args, **kwargs):

        if 'usuario' not in request.session:
            messages.error(request, 'No estás logeado')
            return redirect(reverse('acceso:acceso'))

        return function(request, *args, **kwargs)

    return wrap