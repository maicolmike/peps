from django.shortcuts import render


# Create your views here.
from django.views.generic import DetailView
from .models import PersonaPEP,Familiar
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado
from .forms import CrearPepForm,CrearFamiliaresForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages



class PersonaPEPDetailView(DetailView):
    model = PersonaPEP
    template_name = 'personasPep/personaPep_detalle.html'
    context_object_name = 'persona'
    
@login_required(login_url='login')
def crearPep(request):
    form = CrearPepForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        persona_pep = form.save()
        persona_pep.save()
        messages.success(request, 'Persona Pep creada con éxito')

        # Redirigir a la página de creación de familiares para este PEP
        return redirect(reverse('crear_Familiares', kwargs={'persona_pep_id': persona_pep.id}))

    return render(request, 'personasPep/crearPep.html', {
        'title': "Crear pep",
        'form': form
    })
    
@login_required(login_url='login')
def crearFamiliares(request, persona_pep_id):
    # Asegurarse de que el persona_pep_id sea válido
    try:
        persona_pep = PersonaPEP.objects.get(id=persona_pep_id)
    except PersonaPEP.DoesNotExist:
        # Manejar el caso en el que el ID no es válido
        messages.error(request, 'El ID de la persona PEP no es válido.')
        return redirect('nombre_de_tu_vista_de_error')
    
    familiares = Familiar.objects.filter(persona_pep=persona_pep)
    form = CrearFamiliaresForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        familiar = form.save(commit=False)
        familiar.persona_pep = persona_pep
        familiar.save()
        messages.success(request, 'Familiar ha sido creado con éxito')
        # Crear una nueva instancia del formulario para reiniciar los campos
        form = CrearFamiliaresForm()
        
    # Agregar información sobre la persona PEP al contexto
    context = {
        'title': "Crear Familiares",
        'form': form,
        'persona_pep': persona_pep,  # Agregar la instancia de persona_pep al contexto
        'familiares': familiares,
    }
    
    return render(request, 'personasPep/crearFamiliares.html', context)
'''
    return render(request, 'personasPep/crearFamiliares2.html', {
        'title': "Crear Familiares",
        'form': form
    })
    
'''