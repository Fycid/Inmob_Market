from django.contrib.auth.mixins	import LoginRequiredMixin #para que se authentique el usuario
from django.shortcuts 			import render
from django.urls 				import reverse_lazy
from django.views.generic 		import ListView, CreateView
from django.views.generic.edit 	import UpdateView, DeleteView
from apps.core.mixins 			import AdminRequiredMixins


from .models 				import Productos
from .forms 				import ProductoForm


def detalle (request):
	context = {}
	return render(request, "productos/detalle.html", context )


class ListarAdmin (LoginRequiredMixin,AdminRequiredMixins,ListView):
	template_name= "productos/admin/listar.html"
	model = Productos
	context_object_name= "productos"


	
	def get_queryset(self):
		#self.request
		return Productos.objects.all().order_by("id")

class MisProductos (LoginRequiredMixin,AdminRequiredMixins,ListView):
	template_name= "productos/admin/listar.html"
	model = Productos
	context_object_name= "productos"

	def get_queryset(self):
		return Productos.objects.filter(usuario_id=self.request.user.id)
	

class NuevoAdmin(LoginRequiredMixin,AdminRequiredMixins,CreateView):
	template_name= "productos/admin/nuevo.html"
	model = Productos
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")

	def form_valid(self, form):
		f=form.save(commit=False)
		f.usuario_id = self.request.user.id
		return super(NuevoAdmin, self).form_valid(form)

class EditarAdmin(UpdateView):
	template_name= "productos/admin/editar.html"
	model = Productos
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")



