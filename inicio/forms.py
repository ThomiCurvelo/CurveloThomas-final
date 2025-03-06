from django import forms
from inicio.models import Tarea

class Agregartarea(forms.Form):
    titulo = forms.CharField(max_length=20)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
class BuscarTareas(forms.Form):
    titulo = forms.CharField(max_length=20, required=False)
    
class Editartareaformulario(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Tarea
        fields = '__all__'

