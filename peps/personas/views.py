from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import DetailView
from .models import PersonaPEP, Familiar
from .forms import CrearPepForm, CrearFamiliaresForm

class PersonaPEPDetailView(DetailView):
    model = PersonaPEP
    template_name = 'personasPep/personaPep_detalle.html'
    context_object_name = 'persona'

@login_required(login_url='login')
def crear_pep(request):
    form = CrearPepForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        persona_pep = form.save()
        persona_pep.save()
        messages.success(request, 'Persona Pep creada con éxito')
        return redirect(reverse('crear_familiares', kwargs={'persona_pep_id': persona_pep.id}))

    return render(request, 'personasPep/crearPep.html', {'title': "Crear pep", 'form': form})

@login_required(login_url='login')
def crear_familiares(request, persona_pep_id):
    persona_pep = get_object_or_404(PersonaPEP, id=persona_pep_id)
    familiares = Familiar.objects.filter(persona_pep=persona_pep)
    form = CrearFamiliaresForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        familiar = form.save(commit=False)
        familiar.persona_pep = persona_pep
        familiar.save()
        messages.success(request, 'Familiar ha sido creado con éxito')

    context = {
        'title': "Crear Familiares",
        'form': form,
        'persona_pep': persona_pep,
        'familiares': familiares,
    }

    return render(request, 'personasPep/crearFamiliares.html', context)

@login_required(login_url='login')
def editar_pep(request, pk):
    persona_pep = get_object_or_404(PersonaPEP, pk=pk)
    form = CrearPepForm(request.POST or None, instance=persona_pep)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Persona Pep actualizada con éxito')
        return redirect(reverse('crear_familiares', kwargs={'persona_pep_id': persona_pep.pk}))

    return render(request, 'personasPep/editarPep.html', {'title': 'Editar Pep', 'form': form, 'persona_pep': persona_pep})

@login_required(login_url='login')
def editar_familiar_pep(request, familiar_id):
    familiar = get_object_or_404(Familiar, id=familiar_id)
    persona_pep = familiar.persona_pep
    form = CrearFamiliaresForm(request.POST or None, instance=familiar)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Familiar de Persona Pep actualizada con éxito')
        return redirect('crear_familiares', persona_pep_id=persona_pep.pk)

    return render(request, 'personasPep/editarFamiliarPep.html', {'persona_pep': persona_pep, 'form': form, 'title': 'Editar Familiar Pep'})