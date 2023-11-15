# urls.py
from django.urls import path
#from .views import PersonaPEPDetailView
from . import views

urlpatterns = [
    path('detallePep/<int:pk>/', views.PersonaPEPDetailView.as_view(), name='persona_detalle'),
    path('crearPep', views.crearPep, name='crear_pep'),
    
    # Agrega otras URLs según tus necesidades
]