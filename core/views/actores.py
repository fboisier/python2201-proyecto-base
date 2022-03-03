

from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from core.models import Actor
from core.forms import ActorForm

class ActoresView(View):
    
    def get(self, request):
        contexto = {
            'form': ActorForm(), 
            'actores' : Actor.objects.all(),
        }
        return render(request, 'core/actores.html', contexto)

    def post(self, request):
        print(request.POST)
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'actores Creado')
            return redirect(reverse('actores'))
        else:
            contexto = {
                'form': form, 
                'actores' : Actor.objects.all(),
            }
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/actores.html', contexto) 

class ActoresDetailView(View):
    
    def get(self, request, id):
        Actores = Actor.objects.get(id=id)
        contexto = {
            'form': ActorForm(instance=Actores), 
            'actores' : Actor.objects.all(),
        }
        return render(request, 'core/actores.html', contexto)

    def post(self, request, id):
        
        Actores = Actor.objects.get(id=id)

        form = ActorForm(request.POST, instance=Actores)
        if form.is_valid():
            form.save()
            messages.success(request, 'actores Editado')
            return redirect(reverse('actores'))
        else:

            contexto = {
                'form': form, 
                'Actoreses' : Actor.objects.all(),
            }

            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/actores.html', contexto) 