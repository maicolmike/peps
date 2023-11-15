from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required # vista basada en funciones que no permita acceder a paginas donde no se ha logeado

from .forms import LoginUser,RegistroUsuario


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html',{
        'title': "Index",
    })
    
def login_view(request):
    form = LoginUser(request.POST or None)
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #username = form.cleaned_data.get('username')
        #password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            
            '''if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])  '''
            return redirect('index')
        else : 
            messages.error(request,'Usuario o contraseña incorrectos')
            
    return render(request, 'usuarios/login.html',{
        'title': "Login",
        'form': form
    })

@login_required(login_url='login') 
def logout_view(request):
    logout(request)
    messages.error(request,'Sesion cerrada')
    #messages.success(request,'Sesion cerrada')
    return redirect('login')

@login_required(login_url='login')    
def register(request):
    '''if request.user.is_authenticated:
        return redirect('index')'''
    
    form = RegistroUsuario(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = form.save() #save () se encuentra en el archivo forms.py
        if user:
            if form.cleaned_data['is_admin'] == '1': #El campo en el formulario html es 1
                #otorgar permisos de administrador
                user.is_staff = True
                user.is_superuser = True
            user.save()
            #username = form.cleaned_data.get('username')
            #tipo_usuario = form.cleaned_data['is_admin']
            #print(tipo_usuario)
            #login(request, user) # se logee el usuario que creamos
            messages.success(request, 'usuario creado')
            return redirect('register')
    
    return render(request, 'usuarios/register.html', {
        'form': form,
        'title': "Registro",
        })
    

'''    
@login_required(login_url='login')
def listarUsuarios(request):
    products = User.objects.all().order_by('id')
    return render(request, 'usuarios/list.html',{
        'title': "Index",
        'products': products,
    })    
'''