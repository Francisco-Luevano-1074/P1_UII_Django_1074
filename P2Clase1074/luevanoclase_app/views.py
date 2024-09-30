from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse('Hola, Nava, respondiendo')

# Create your views here.
