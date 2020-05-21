from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("inicio")
def about(request):
    return HttpResponse("Historia")
def services(request):
    return HttpResponse("Servicios")
def store(request):
    return HttpResponse("Visitanos")
def contact(request):
    return HttpResponse("Contacto")
def blog(request):
    return HttpResponse("Blog")
def sample(request):
    return HttpResponse("Sample")

# Create your views here.
