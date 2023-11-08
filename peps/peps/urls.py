from django.contrib import admin
from django.urls import path
#instaladas por mi
from . import views 
from django.urls import include
from users.views import UsersListView,UserUdpateView,UserUdpateClave


urlpatterns = [
    path('admin/', admin.site.urls),
    #instaladas por mi
    path('',views.index, name='index'),
    path('usuarios/registro',views.register, name='register'),
    path('usuarios/login',views.login_view, name='login'),
    path('usuarios/logout',views.logout_view, name='logout'),
    path('usuarios/list',UsersListView.as_view(), name='listarUsuarios'),
    path('usuarios/editar', UserUdpateView, name='updateusuarios'),
    path('usuarios/editarClave', UserUdpateClave, name='updateusuariosClave'),
]