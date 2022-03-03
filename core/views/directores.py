

from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from core.models import Director
from core.forms import DirectorForm

class DirectorView(View):
    
    def get(self, request):
        contexto = {
            'form': DirectorForm(), 
            'directores' : Director.objects.all(),
        }
        return render(request, 'core/directores.html', contexto)

    def post(self, request):
        print(request.POST)
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Director Creado')
            return redirect(reverse('directores'))
        else:
            contexto = {
                'form': form, 
                'directores' : Director.objects.all(),
            }
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/directores.html', contexto) 

class DirectorDetailView(View):
    
    def get(self, request, id):
        director = Director.objects.get(id=id)
        contexto = {
            'form': DirectorForm(instance=director), 
            'directores' : Director.objects.all(),
        }
        return render(request, 'core/directores.html', contexto)

    def post(self, request, id):
        
        director = Director.objects.get(id=id)

        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            messages.success(request, 'Director Editado')
            return redirect(reverse('directores'))
        else:

            contexto = {
                'form': form, 
                'directores' : Director.objects.all(),
            }

            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/directores.html', contexto) 