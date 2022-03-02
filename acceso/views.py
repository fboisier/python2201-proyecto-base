from django import forms
from django.shortcuts import redirect, render
from django.db.models import Q
from django.urls import reverse
from django.views import View
from django.contrib import messages
from acceso.forms import UsuarioForm
from acceso.models import Usuario
import bcrypt
# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField(
                    label='Usuario', 
                    max_length=50, 
                    required=True, 
                    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario o Email'})
                )

    password = forms.CharField(
                    label='Contraseña', 
                    required=True, 
                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'})
                )



class LoginView(View):
    
    def get(self, request):

        if 'usuario' in request.session:
            messages.error(request, 'YA ESTAS LOGEADO. Si quieres salir, CLICK EN SALIR!!')
            return redirect('/')

        contexto = {
            'formRegister': UsuarioForm(),
            'formLogin': LoginForm()
        }

        return render(request, 'acceso/login.html', contexto)

    def post(self, request):
        print(request.POST)

        form = UsuarioForm(request.POST)

        if form.is_valid():
            
            usuario = form.save(commit=False)
            usuario.password = bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()
            
            messages.success(request, 'Usuario creado correctamente')
            return redirect(reverse('acceso:acceso'))
        else:

            contexto = {
                'formRegister': form,
                'formLogin': LoginForm()
            }

            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'acceso/login.html', contexto) 


def login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            
            user = Usuario.objects.filter(Q(username=form.cleaned_data['username'])| Q(email=form.cleaned_data['username'])).first()
            if user:
                form_password = form.cleaned_data['password']
                if bcrypt.checkpw(form_password.encode(), user.password.encode()):
                    
                    request.session['usuario'] = { 'nombre' : user.nombre, 'email' : user.email, 'username' : user.username, 'id': user.id }
                    return redirect('/')
                else:
                    messages.error(request, '1Contraseña o Email o Nombre de Usuario INCORRECTO')
            else:
                messages.error(request, '2Contraseña o Email o Nombre de Usuario INCORRECTO')

            return redirect(reverse('acceso:acceso'))
        else:
            contexto = {
                'formRegister': UsuarioForm(),
                'formLogin': form
            }
            return render(request, 'acceso/login.html', contexto) 

def logout(request):

    if 'usuario' in request.session:
        messages.success(request, 'SALISTE')
        del request.session['usuario']
    else:
        messages.error(request, 'Tu no estas logeado.')

    return redirect(reverse('acceso:acceso'))