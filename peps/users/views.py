from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic.list import ListView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin # vista basada en clases que no permita acceder a paginas donde no se ha logeado
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado
from django.contrib import messages
import time # módulo time de Python, es parte de la biblioteca estándar de Python, y contiene la útil función sleep() que suspende o detiene un programa durante un número de determinado de segundos
from peps.forms import CambiarClaveForm
from django.contrib.auth import update_session_auth_hash


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
        context['title'] = 'Listado de Usuarios'
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
            user = User.objects.get(id=user_id) #En contraste, si tuvieras un objeto User específico (por ejemplo, obtenido de una consulta a la base de datos), podrías hacer user.set_password(password_nueva) y user.save() para cambiar la contraseña de ese usuario en particular. Esto podría ser útil en situaciones donde estás trabajando con información específica de un usuario, independientemente de la sesión actual.

            # Establece la nueva contraseña usando set_password()
            user.set_password(new_password)

            # Guarda el usuario, lo que encripta la nueva contraseña
            user.save()
            
            # Actualizar la sesión del usuario para evitar cerrar sesión después de cambiar la contraseña
            update_session_auth_hash(request, user)
            
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
    
@login_required(login_url='login')    
def CambiarClave(request):
    
    form = CambiarClaveForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        password_actual = form.cleaned_data['passwordActual']
        password_nueva = form.cleaned_data['passwordNew']
        confirmar_password = form.cleaned_data['passwordNewConfirm']

        # Validar que la contraseña actual sea correcta
        if not request.user.check_password(password_actual):
            messages.error(request, 'La contraseña actual es incorrecta.')
            return render(request, 'usuarios/cambiarClave.html', {'form': form, 'title': 'Cambiar clave'})
        
        # Validar que la contraseña actual sea diferente de la nueva
        if password_actual == password_nueva:
            messages.error(request, 'La nueva contraseña debe ser diferente de la contraseña actual.')
            return render(request, 'usuarios/cambiarClave.html', {'form': form, 'title': 'Cambiar clave'})
        
        # Validar que la nueva contraseña y la confirmación coincidan
        if password_nueva != confirmar_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'usuarios/cambiarClave.html', {'form': form, 'title': 'Cambiar clave'})

        # Cambiar la contraseña del usuario
        request.user.set_password(password_nueva)   #request.user es específico para interactuar con el usuario que ha iniciado sesión en ese momento, 
        request.user.save()

        # Actualizar la sesión del usuario para evitar cerrar sesión después de cambiar la contraseña
        update_session_auth_hash(request, request.user)

        messages.success(request, 'Contraseña cambiada exitosamente.')

    return render(request, 'usuarios/cambiarClave.html', {'form': form, 'title': 'Cambiar clave'})