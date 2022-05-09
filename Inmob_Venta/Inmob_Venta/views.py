from django.shortcuts 			import render
from django.contrib.auth.decorators import login_required #basado en funcion
from django.views.generic.base  import TemplateView
from django.views.generic 			import ListView
from apps.productos.models 		import Productos


"""
#Inicio basado en funcion
#@login_required
def inicio (request):
	context = {		
		"productos":Productos.objects.all()
	}
	return render(request,"inicio.html", context)

class Inicio(TemplateView):
	template_name = "inicio.html" 
	

	
	def get_context_data(self, ** kwargs):
		context = super (Inicio, self).get_context_data(** kwargs)
		context ["productos"] = Productos.objects.all()
		return context
	
"""
class Inicio (ListView):
	template_name= "inicio.html"
	model = Productos
	context_object_name= "productos"
	paginate_by=3


	def get_queryset(self):
		return Productos.objects.filter(Estado__in=[1,2,4])