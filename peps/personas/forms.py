from django.forms import ModelForm
from .models import PersonaPEP
from django import forms


'''
class CrearPepForm(ModelForm):
    class Meta:
        model = PersonaPEP
        fields = [
            'nombre', 'identificacion', 'es_pep', 'estado', 'tipo_pep', 'cargo', 'fecha_vinculacion', 'fecha_desvinculacion', 'cuentas_extranjeras', 'fecha_registro_pep', 'fecha_actualizacion'
        ]
        labels = {
            'nombre': 'Nombres y apellidos'
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre'
        }) #Dic
        
'''       

class CrearPepForm(ModelForm):
    class Meta:
        model = PersonaPEP
        fields = [
            'nombre', 'identificacion', 'es_pep', 'estado', 'tipo_pep', 'cargo', 'fecha_vinculacion', 'fecha_desvinculacion', 'cuentas_extranjeras', 'fecha_registro_pep', 'fecha_actualizacion'
        ]
        labels = {
            'nombre': 'Nombres y apellidos'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identificacion'}),
            'estado': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Seleccionar'), ('Asociado', 'Asociado'), ('No asociado', 'No asociado'), ('Retirado', 'Retirado')]),
            
            

        }