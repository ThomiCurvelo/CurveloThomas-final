from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.titulo}'
