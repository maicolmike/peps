from django.urls import path
from . import views

urlpatterns = [
    path('detallePep/<int:pk>/', views.PersonaPEPDetailView.as_view(), name='persona_detalle'),
    path('crearPep/', views.crearPep, name='crear_pep'),
    path('crearFamiliares/<int:persona_pep_id>/', views.crearFamiliares, name='crear_Familiares'),
    path('editarPep/<int:pk>/', views.editarPep, name='editar_pep'),  # Nueva URL para la edición
]