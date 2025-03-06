from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)  # Campo a elección
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
