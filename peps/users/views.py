from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import User



class ProductListView(ListView):
    template_name = 'index.html'
    queryset = User.objects.all().order_by('id')
    print(queryset)
    paginate_by = 1
