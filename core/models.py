from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.age})"


class Pelicula(models.Model):

    CLASIFICACION_CHOICES = (
        ('F', 'MENOR DE EDAD'),
        ('A', 'MAYOR DE EDAD'),
    )

    GENERO_CHOISES  = (
        ('A', 'Accion'),
        ('D', 'Drama'),
        ('C', 'Comedia'),
        ('S', 'Suspenso'),
        ('T', 'Terror'),
        ('O', 'Otro'),
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_de_estreno = models.DateField()
    duracion = models.IntegerField()
    calificacion = models.IntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOISES, default='A')
    clasificacion = models.CharField(max_length=1, choices=CLASIFICACION_CHOICES, default='F')
    director = models.ForeignKey(Director,related_name='peliculas', on_delete=models.CASCADE)
    estado = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo

class Actor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    peliculas = models.ManyToManyField(Pelicula, related_name='actores')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name