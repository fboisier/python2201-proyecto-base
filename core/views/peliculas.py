

from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from core.models import Pelicula
from core.forms import PeliculaForm

class PeliculasView(View):
    
    def get(self, request):
        contexto = {
            'form': PeliculaForm(), 
            'peliculas' : Pelicula.objects.all(),
        }
        return render(request, 'core/peliculas.html', contexto)

    def post(self, request):
        print(request.POST)
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pelicula Creado')
            return redirect(reverse('peliculas'))
        else:
            contexto = {
                'form': form, 
                'peliculas' : Pelicula.objects.all(),
            }
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/peliculas.html', contexto) 

class PeliculasDetailView(View):
    
    def get(self, request, id):
        director = Pelicula.objects.get(id=id)
        contexto = {
            'form': PeliculaForm(instance=director), 
            'peliculas' : Pelicula.objects.all(),
        }
        return render(request, 'core/peliculas.html', contexto)

    def post(self, request, id):
        
        director = Pelicula.objects.get(id=id)

        form = PeliculaForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pelicula Editado')
            return redirect(reverse('peliculas'))
        else:

            contexto = {
                'form': form, 
                'peliculas' : Pelicula.objects.all(),
            }

            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'core/peliculas.html', contexto) 