from django.conf import settings
from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    introduccion = models.TextField()
    imagen = models.URLField(blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    actualidad = models.TextField(blank=True, null=True)
    socios = models.IntegerField(blank=True, null=True)
    puntaje = models.IntegerField(blank=True, null=True)

        
    def __str__(self):
        return self.titulo


