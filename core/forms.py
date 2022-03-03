

from django import forms

from core.models import Actor, Director, Pelicula

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'fecha_de_estreno', 'duracion', 'genero','calificacion', 'clasificacion', 'director', 'estado']

        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripcion',
            'fecha_de_estreno': 'Fecha de estreno',
            'duracion': 'Duracion',
            'genero': 'Genero',
            'calificacion': 'Calificacion',
            'clasificacion': 'Clasificacion',
            'director': 'Director',
            'estado': 'Estado',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_de_estreno': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'calificacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-select'}),
            'director': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'age', 'peliculas']

        labels = {
            'name': 'Nombre',
            'age': 'Edad',
            'peliculas': 'Peliculas',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'peliculas': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'age']

        labels = {
            'name': 'Nombre',
            'age': 'Edad',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }
