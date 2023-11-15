from django.shortcuts import render


# Create your views here.
from django.views.generic import DetailView
from .models import PersonaPEP
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado
from .forms import CrearPepForm



class PersonaPEPDetailView(DetailView):
    model = PersonaPEP
    template_name = 'personasPep/personaPep_detalle.html'
    context_object_name = 'persona'
    
@login_required(login_url='login')
def crearPep(request):
    
    form = CrearPepForm
    
    return render(request, 'personasPep/crearPep.html',{
        'title': "Crear pep",
        'form': form
        
    })    