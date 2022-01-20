from django.shortcuts 		import render
from django.views.generic 	import ListView, CreateView
from django.urls 			import reverse_lazy
from .models 				import Productos
from .forms 				import ProductoForm


def detalle (request):
	context = {}
	return render(request,"productos/detalle.html",context )


class ListarAdmin (ListView):
	template_name="productos/admin/listar.html"
	model = Productos
	context_object_name="productos"


	"""
	def get_queryset(self):
		#self.request
		return Productos.objects.filter(id=2)
	"""

class NuevoAdmin(CreateView):
	template_name= "productos/admin/nuevo.html"
	model = Productos
	form_class = ProductoForm

	def get_success_url(**Kwargs):
		return reverse_lazy("productos : admin_listar")