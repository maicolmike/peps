from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic.list import ListView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin # vista basada en clases que no permita acceder a paginas donde no se ha logeado
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado
from django.contrib import messages


class UsersListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    template_name = 'usuarios/list.html'
    queryset = User.objects.all().order_by('id')
    #print(queryset)
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Usuarios'
        #print(context) # para saber que variable debe tener en este caso son object_list o user_list
        #context['usersList']=context['user_list']
        
        return context
    
@login_required(login_url='login')    
def UserUdpateView(request):
    
    if request.method == 'POST':
        id =request.POST.get('id')
        nombre = request.POST.get('username')
        email = request.POST.get('userEmail')
        tipousuario = request.POST.get('tipousuario')
        
        # Llama a tu función personalizada con los datos
        #resultado = nombre,email,tipousuario,id # para comprobar que si se esten pasando los datos
        
        # Devuelve una respuesta, por ejemplo, un mensaje
        #return HttpResponse(f'El resultado es: {resultado}')
    
    # Busca el usuario en la base de datos por su ID
        try:
            user = User.objects.get(id=id)

            # Actualiza los campos con los nuevos valores
            user.email = email
            user.is_superuser = tipousuario

            # Guarda los cambios en la base de datos
            user.save()

            #resultado = "Usuario actualizado correctamente."
        except user.DoesNotExist:
            resultado = "El usuario no existe."

        #return HttpResponse(f'Resultado: {resultado}')
        return redirect('listarUsuarios')

    #return render(request, 'editarPruebas.html')