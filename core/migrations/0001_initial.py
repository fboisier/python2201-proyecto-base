# Generated by Django 4.0.2 on 2022-03-03 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_de_estreno', models.DateField()),
                ('duracion', models.IntegerField()),
                ('calificacion', models.IntegerField()),
                ('genero', models.CharField(choices=[('A', 'Accion'), ('D', 'Drama'), ('C', 'Comedia'), ('S', 'Suspenso'), ('T', 'Terror'), ('O', 'Otro')], default='A', max_length=1)),
                ('clasificacion', models.CharField(choices=[('F', 'MENOR DE EDAD'), ('A', 'MAYOR DE EDAD')], default='F', max_length=1)),
                ('estado', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peliculas', to='core.director')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('peliculas', models.ManyToManyField(related_name='actores', to='core.Pelicula')),
            ],
        ),
    ]
