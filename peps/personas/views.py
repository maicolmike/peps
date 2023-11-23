from django.shortcuts import render,get_object_or_404


# Create your views here.
from django.views.generic import DetailView
from .models import PersonaPEP,Familiar
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado
from .forms import CrearPepForm,CrearFamiliaresForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin #vistas basada en clases
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView,DeleteView



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
    persona_pep = get_object_or_404(PersonaPEP, id=persona_pep_id)
    familiares = Familiar.objects.filter(persona_pep=persona_pep)
    form = CrearFamiliaresForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        familiar = form.save(commit=False)
        familiar.persona_pep = persona_pep
        familiar.save()
        messages.success(request, 'Familiar ha sido creado con éxito')
        form = CrearFamiliaresForm()

    context = {
        'title': "Crear Familiares",
        'form': form,
        'persona_pep': persona_pep,
        'familiares': familiares,
    }

    return render(request, 'personasPep/crearFamiliares.html', context)

@login_required(login_url='login')
def editarPep(request, pk):
    persona_pep = get_object_or_404(PersonaPEP, pk=pk)
    form = CrearPepForm(request.POST or None, instance=persona_pep)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Persona Pep actualizada con éxito')

        return redirect(reverse('crear_Familiares', kwargs={'persona_pep_id': persona_pep.pk}))

    return render(request, 'personasPep/editarPep.html', {'title': 'Editar Pep', 'form': form, 'persona_pep': persona_pep})

class ShippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    login_url = 'login'
    model = PersonaPEP
    form_class = CrearPepForm
    template_name = 'personasPep/editarPep.html'
    
    def get_success_url(self):
        return reverse('shipping_addresses:shipping_addresses')