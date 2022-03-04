from django.shortcuts 			import render
from django.urls 				import reverse_lazy
from django.views.generic 		import ListView, CreateView
from django.views.generic.edit 	import UpdateView



from .models 				import Productos
from .forms 				import ProductoForm


def detalle (request):
	context = {}
	return render(request, "productos/detalle.html", context )


class ListarAdmin (ListView):
	template_name= "productos/admin/listar.html"
	model = Productos
	context_object_name= "productos"


	"""
	def get_queryset(self):
		#self.request
		return Productos.objects.filter(id=2)
	"""

class NuevoAdmin(CreateView):
	template_name= "productos/admin/nuevo.html"
	model = Productos
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos : admin_listar")

class EditarAdmin(UpdateView):
	template_name= "productos/admin/editar.html"
	model = Productos
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos : admin_listar")