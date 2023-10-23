from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html',{
        'message': 'hola mundo desde el contexto',
        'products': [
            {'title':'playera', 'price':5,'stock':True },
            {'title':'camisa', 'price':11,'stock':False },
        ]
    })