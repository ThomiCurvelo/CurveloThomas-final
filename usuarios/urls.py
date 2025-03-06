from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login, registro, ver_perfil, editar_perfil, CambiarPasswordView
#editar_perfil


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    #path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('perfil/', ver_perfil, name='ver_perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', CambiarPasswordView.as_view(), name='cambiar_password'),
]
