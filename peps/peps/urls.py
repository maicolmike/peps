"""
URL configuration for peps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#instaladas por mi
from . import views 
from django.urls import include
from users.views import ProductListView


urlpatterns = [
    path('admin/', admin.site.urls),
    #instaladas por mi
    path('',views.index, name='index'),
    #path('',ProductListView.as_view(), name='index'),
    path('usuarios/registro',views.register, name='register'),
    path('usuarios/login',views.login_view, name='login'),
    path('usuarios/logout',views.logout_view, name='logout'),
    path('usuarios/listarUsuarios',views.listarUsuarios, name='listarUsuarios'),
]