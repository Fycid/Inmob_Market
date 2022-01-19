from django.shortcuts 			import render

from django.views.generic.base  import TemplateView

from apps.productos.models 		import Productos

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

#Inicio basado en funcion 
def inicio (request):
	context = {		
		"productos":Productos.objects.all()
	}
	return render(request,"inicio.html", context)

"""
class Inicio(TemplateView):
	template_name = "inicio.html" 

	
	def get_context_data(self, ** kwargs):
		context = super (Inicio, self).get_context_data(** kwargs)
		context ["productos"] = Productos.objects.all()
		return context
	
