from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def inicio(request):
    paises = "colombia"
    ahora = datetime.datetime.now()
    persona = {
        "nombre": "Jair",
        "apellido": "Prada",
        "edad": 20,
        "fecha":ahora
    }
    return render(request,"vistas/home.html",persona)

def probabilidadMapa(request):
    return render(request,"vistas/probabilidadMapa.html")

def calcular(request):
    return render(request,"vistas/calcularProbabilidad.html")
def nosotros(request):
    return render(request,'vistas/nosotros.html')