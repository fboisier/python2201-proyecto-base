from django.urls import path

from core.views.directores import DirectorDetailView, DirectorView
from core.views.actores import ActoresView, ActoresDetailView
from core.views.peliculas import PeliculasView, PeliculasDetailView
from .views.index import index

urlpatterns = [
    path('', index, name="index"),

    path('directores/', DirectorView.as_view(), name='directores' ),
    path('directores/<int:id>/', DirectorDetailView.as_view(), name='directores_editar' ),

    path('actores/', ActoresView.as_view(), name='actores' ),
    path('actores/<int:id>/', ActoresDetailView.as_view(), name='actores_editar' ),

    path('peliculas/', PeliculasView.as_view(), name='peliculas' ),
    path('peliculas/<int:id>/', PeliculasDetailView.as_view(), name='peliculas_editar' ),
]
