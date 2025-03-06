from django.urls import path
from inicio.views import inicio, agregar_tarea, listar_tarea, detalle_tarea, borrar_tarea, Editar_tarea, Borrartarea


urlpatterns = [
    path('', inicio, name="inicio"),
    path('agregar_tarea/', agregar_tarea, name="agregar_tarea"),
    path('listar_tarea/', listar_tarea, name="listar_tarea"),
    path('ver_tarea/<int:id>/', detalle_tarea, name='detalle_tarea'),
    #path('borrar_tarea/<int:id>', borrar_tarea, name='borrar_tarea'),
    path('editar_tarea/<int:pk>', Editar_tarea.as_view() , name="editar_tarea"),
    path('borrar_tarea/<int:pk>', Borrartarea.as_view() , name="borrar_tarea"),
]
