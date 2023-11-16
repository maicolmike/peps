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
            'nombre': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Nombre','id': 'nombre'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identificacion','id': 'identificacion'}),
            'estado': forms.Select(attrs={'id': 'estado','class': 'form-control'}, choices=[('', 'Seleccionar'), ('Asociado', 'Asociado'), ('No asociado', 'No asociado'), ('Retirado', 'Retirado')]),
            'tipo_pep': forms.Select(attrs={'id': 'tipo_pep','class': 'form-control'}, choices=[('', 'Seleccionar'), ('Maneja recursos publicos nacionales', 'Maneja recursos públicos nacionales'), ('Maneja recursos publicos exterior', 'Maneja recursos públicos exterior'), ('Funcion publica prominente', 'Función pública prominente'), ('Reconocimiento Publico', 'Reconocimiento Público')]),
            'cargo': forms.TextInput(attrs={'id': 'cargo','class': 'form-control', 'placeholder': 'cargo'}),
            'fecha_vinculacion': forms.DateInput(attrs={'id': 'fecha_vinculacion','class': 'form-control datepicker', 'placeholder': 'Fecha de vinculación'}),
            'fecha_desvinculacion': forms.DateInput(attrs={'id': 'fecha_desvinculacion','class': 'form-control datepicker', 'placeholder': 'Fecha de desvinculación'}),
            'fecha_registro_pep': forms.DateInput(attrs={'id': 'fecha_registro_pep','class': 'form-control datepicker', 'placeholder': 'Fecha de registro pep'}),
            'fecha_actualizacion': forms.DateInput(attrs={'id': 'fecha_actualizacion','class': 'form-control datepicker', 'placeholder': 'Fecha de actualizacion'}),
            'es_pep': forms.RadioSelect(attrs={'id': 'es_pep','class': ''}, choices=[(True, 'Sí'), (False, 'No')]),
            'cuentas_extranjeras': forms.RadioSelect(attrs={'id': 'cuentas_extranjeras','class': ''}, choices=[(True, 'Sí'), (False, 'No')]),
        }