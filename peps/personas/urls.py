# urls.py
from django.urls import path
#from .views import PersonaPEPDetailView
from . import views

urlpatterns = [
    path('pep/<int:pk>/', views.PersonaPEPDetailView.as_view(), name='persona_detail'),
    # Agrega otras URLs según tus necesidades
]