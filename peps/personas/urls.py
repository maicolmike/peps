# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('detallePep/<int:pk>/', views.PersonaPEPDetailView.as_view(), name='persona_detalle'),
    path('crearPep/', views.crear_pep, name='crear_pep'),  
    path('crearFamiliares/<int:persona_pep_id>/', views.crear_familiares, name='crear_familiares'),  
    path('editarPep/<int:pk>/', views.editar_pep, name='editar_pep'),  
    path('editarFamiliarPep/<int:familiar_id>/', views.editar_familiar_pep, name='editar_familiar_pep'), 
    path('eliminarFamiliarPep/<int:familiar_id>/', views.eliminar_familiar_pep, name='eliminar_familiar_pep'),
    path('eliminar_persona_pep/<int:persona_pep_id>/', views.eliminar_persona_pep, name='eliminar_persona_pep'),
    path('consultarPep/', views.consultar_pep, name='consultar_pep'),  
]