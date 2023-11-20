# personas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('detallePep/<int:pk>/', views.PersonaPEPDetailView.as_view(), name='persona_detalle'),
    path('crearPep/', views.crearPep, name='crear_pep'),
    path('crearFamiliares/<int:persona_pep_id>/', views.crearFamiliares, name='crear_Familiares'),  # Asegúrate de agregar el parámetro persona_pep_id
]