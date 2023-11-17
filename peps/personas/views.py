from django.shortcuts import render


# Create your views here.
from django.views.generic import DetailView
from .models import PersonaPEP,Familiar
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado
from .forms import CrearPepForm,CrearFamiliaresForm
from django.contrib import messages



class PersonaPEPDetailView(DetailView):
    model = PersonaPEP
    template_name = 'personasPep/personaPep_detalle.html'
    context_object_name = 'persona'
    
@login_required(login_url='login')
def crearPep(request):
    
    form = CrearPepForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        PersonaPEP = form.save()
        PersonaPEP.save()
        messages.success(request,'Persona Pep creada con exito')
    
    return render(request, 'personasPep/crearPep.html',{
        'title': "Crear pep",
        'form': form
        
    })    
    
    
@login_required(login_url='login')
def crearFamiliares(request):
    
    form = CrearFamiliaresForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        Familiar = form.save()
        Familiar.save()
        messages.success(request,'Familiar ha sido creada con exito')
    
    return render(request, 'personasPep/crearFamiliares.html',{
        'title': "Crear Familiares",
        'form': form
        
    })    