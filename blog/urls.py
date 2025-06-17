from django.urls import path
from . import views

urlpatterns = [
    path('evaluacion2', views.lista_publicaciones, name='lista_public'),
]