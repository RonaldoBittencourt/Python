from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def produto_home(request):
    return HttpResponse("Bem-vindo à página de produtos!");
