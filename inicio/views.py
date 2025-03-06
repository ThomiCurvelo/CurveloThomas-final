from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Tarea
from inicio.forms import Agregartarea, BuscarTareas, Editartareaformulario
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin





def inicio(request):
    #return HttpResponse("<h1>Esta es mi primera vista</h1>")
    return render(request, 'inicio/inicio.html')

def agregar_tarea(request):
    formulario = Agregartarea()
    if request.method == "POST":
        formulario = Agregartarea(request.POST)
        if formulario.is_valid():
            print('Cleaned data:', formulario.cleaned_data)
            titulo = Tarea(
                titulo=formulario.cleaned_data.get('titulo'),
                descripcion=formulario.cleaned_data.get('descripcion'),
                fecha_creacion=formulario.cleaned_data.get('fecha_creacion')
            )
            titulo.save()
            return redirect("listar_tarea")
    return render(request, 'inicio/agregar_tarea.html', {'formulario': formulario})

def listar_tarea(request):
    formulario = BuscarTareas(request.GET) 
    
    if formulario.is_valid():
        titulo = formulario.cleaned_data.get('titulo')  
        titulo = Tarea.objects.filter(titulo__icontains=titulo)  
    else:
        titulo = Tarea.objects.all()
    
    return render(request, 'inicio/listar_tarea.html', {'titulo': titulo, 'formulario': formulario})

def detalle_tarea(request, id):
    titulo = Tarea.objects.get(id=id)
    return render(request, 'inicio/detalle_tarea.html', {'titulo':titulo})

def borrar_tarea(request, id):
    titulo = Tarea.objects.get(id=id)
    titulo.delete()
    return redirect("listar_tarea")

class Editar_tarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    template_name = "inicio/editar_tarea.html"
    success_url =  reverse_lazy("listar_tarea")
    form_class = Editartareaformulario

class Borrartarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "inicio/borrar_tarea.html"
    success_url =  reverse_lazy("listar_tarea")
