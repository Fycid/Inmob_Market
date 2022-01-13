from django.shortcuts import render
from apps.productos.models import Productos

"""
def inicio (request):
	productos = Productos.objects.all()

	usuario = {

		"nombre": "Fabian",
		"apellido": "Cid"	
	}

	context = {
		"usuario": usuario,
		"productos":productos
	}
	return render(request,"inicio.html", context)

def login (request):
	return render(request,"login.html")

"""
def inicio (request):
	context = {		
		"productos":Productos.objects.all()
	}
	return render(request,"inicio.html", context)
