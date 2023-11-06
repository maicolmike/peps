from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin # vista basada en clases que no permita acceder a paginas donde no se ha logeado



class UsersListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    template_name = 'usuarios/list.html'
    queryset = User.objects.all().order_by('id')
    #print(queryset)
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Usuarios'
        #print(context) # para saber que variable debe tener en este caso son object_list o user_list
        #context['usersList']=context['user_list']
        
        return context