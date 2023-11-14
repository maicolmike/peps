from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic.list import ListView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin # vista basada en clases que no permita acceder a paginas donde no se ha logeado
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado
from django.contrib import messages
import time # módulo time de Python, es parte de la biblioteca estándar de Python, y contiene la útil función sleep() que suspende o detiene un programa durante un número de determinado de segundos

# esta Clase sirve para listar los usuarios que se obtienen de la vista listar usuarios
# esta asociada a los siguiente template-usuarios-list.html peps-peps-urls.py  
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
    
# esta funcion sirve para editar los usuarios que se obtienen de la vista listar usuarios
# esta asociada a los siguiente template-usuarios-list.html peps-peps-urls.py      
@login_required(login_url='login')    
def UserUdpateView(request):
    
    if request.method == 'POST':
        user_id =request.POST.get('id')
        nombre = request.POST.get('username')
        email = request.POST.get('userEmail')
        tipousuario = request.POST.get('tipousuario')
        
    # Busca el usuario en la base de datos por su ID
        try:
            user = User.objects.get(id=user_id)

            # Actualiza los campos con los nuevos valores
            user.email = email
            user.is_superuser = tipousuario

            # Guarda los cambios en la base de datos
            user.save()

        except user.DoesNotExist:
            resultado = "El usuario no existe."

        time.sleep(1.5) #funcion para que se demore en redireccionar
        return redirect('listarUsuarios')

# esta funcion sirve para actualizar la clave los usuarios que se obtienen de la vista listar usuarios
# esta asociada a los siguiente template-usuarios-list.html peps-peps-urls.py  
@login_required(login_url='login')    
def UserUdpateClave(request):
    
    if request.method == 'POST':
        user_id = request.POST.get('id')
        new_password = request.POST.get('passnew')

        try:
            # Obtén el usuario de la base de datos
            user = User.objects.get(id=user_id)

            # Establece la nueva contraseña usando set_password()
            user.set_password(new_password)

            # Guarda el usuario, lo que encripta la nueva contraseña
            user.save()
            
        except User.DoesNotExist:
            resultado = "El usuario no existe."
            
        time.sleep(1.5) #funcion para que se demore en redireccionar
        return redirect('listarUsuarios')
    
# esta funcion sirve para eliminar los usuarios que se obtienen de la vista listar usuarios
# esta asociada a los siguiente template-usuarios-list.html peps-peps-urls.py  
@login_required(login_url='login')    
def UserDelete(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        
        # Busca el usuario en la base de datos por su ID
        try:
            user = User.objects.get(id=user_id)

            # Elimina el usuario de la base de datos
            user.delete()

        except User.DoesNotExist:
            resultado = "El usuario no existe."

        # Redirecciona a la lista de usuarios después de eliminar
        time.sleep(1.5) #funcion para que se demore en redireccionar
        return redirect('listarUsuarios')