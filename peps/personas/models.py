from django.db import models

# Create your models here.
class PersonaPEP(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    es_pep = models.BooleanField(default=False)
    estado = models.CharField(max_length=50)
    tipo_pep = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_vinculacion = models.DateField()
    fecha_desvinculacion = models.DateField(null=True, blank=True)
    cuentas_extranjeras = models.BooleanField(default=False)
    fecha_registro_pep = models.DateField()
    fecha_actualizacion = models.DateField()
    
    def __str__(self):
        return self.nombre

class Familiar(models.Model):
    persona_pep = models.ForeignKey(PersonaPEP, on_delete=models.CASCADE, related_name='familiares')
    nombre = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre