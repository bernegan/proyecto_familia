from django.urls import URLPattern, path
from . import views


urlpatterns = [

       path('bddfamilia/<nombre>/<int:edad>/<nacimiento>/<int:telefono>/' , views.Familiar),
       path('lista_familia/' , views.Lista_familia)
       
]