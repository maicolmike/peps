from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from .models import PersonaPEP

class PersonaPEPDetailView(DetailView):
    model = PersonaPEP
    template_name = 'personasPep/personaPep_detalle.html'
    context_object_name = 'persona'