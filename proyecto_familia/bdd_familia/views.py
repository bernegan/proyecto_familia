from django.shortcuts import render
from django.http import HttpResponse
from bdd_familia.models import Familia
from django.shortcuts import render


# Create your views here.

#Vista para cargar los datos a la BDD
def Familiar(request, nombre , edad , nacimiento , telefono):
    familiar = Familia(nombre = nombre , edad = edad , nacimiento = nacimiento , telefono = telefono)
    familiar.save()
    texto = f'Se guardo en la BDD familiar a: {familiar.nombre}\n Edad: {familiar.edad}\n Nacimiento: {familiar.nacimiento}\n Numero de telefono: {familiar.telefono}'
    return HttpResponse(texto)




#Vista para mostrar los datos familiares en la pagina web
def Lista_familia(request):
    lista_familia = Familia.objects.all()
    diccionario = {'lista_familia': lista_familia}                      
    return render(request , 'plantillafamilia.html',diccionario)


def Bootstrap(request):

    return render(request , 'index.html')

    
