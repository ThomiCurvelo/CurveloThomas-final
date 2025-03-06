from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from usuarios.forms import NuestroUserCreationForm, NuestroUserChangeForm, PerfilForm
from django.contrib.auth import login as django_login
from usuarios.models import InfoExtra, Perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario = NuestroUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = NuestroUserCreationForm()
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        formulario = NuestroUserChangeForm(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
                
            info_extra.save()
                
            formulario.save()
            return redirect('inicio')
    else:
        formulario = NuestroUserChangeForm(instance=request.user, initial={'avatar': info_extra.avatar})
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

@login_required
def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'usuarios/ver_perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})

class CambiarPasswordView(PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('ver_perfil')