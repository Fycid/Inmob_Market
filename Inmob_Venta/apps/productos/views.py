from django.contrib.auth.mixins		import LoginRequiredMixin #para que se authentique el usuario
from django.shortcuts 				import render
from django.urls 					import reverse_lazy
from django.views.generic 			import ListView, CreateView
from django.views.generic.edit 		import UpdateView, DeleteView
from django.views.generic.detail 	import DetailView
from apps.core.mixins 				import AdminRequiredMixins


from .models 				import Productos
from .forms 				import ProductoForm

"""
def detalle (request):
	context = {}
	return render(request, "productos/detalle.html", context )
"""

class ListarAdmin (LoginRequiredMixin,AdminRequiredMixins,ListView):
	template_name= "productos/admin/listar.html"
	model = Productos
	context_object_name= "productos"
	paginate_by=3


	def get_context_data(self, ** kwargs):
		context = super (ListarAdmin, self).get_context_data(** kwargs)
		context ["nombre_buscado"] = self.request.GET.get("nombre_producto","")
		return context

	def get_queryset(self):
		busqueda_nombre = self.request.GET.get("nombre_producto","")
		query = Productos.objects.all().order_by("nombre")
		if len(busqueda_nombre) > 0:
			query = query.filter(nombre__icontains=busqueda_nombre)
		return query 

class MisProductos (LoginRequiredMixin,AdminRequiredMixins,ListView):
	template_name= "productos/admin/listar.html"
	model = Productos
	context_object_name= "productos"
	paginate_by=1


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

class EditarAdmin(LoginRequiredMixin,AdminRequiredMixins,UpdateView):
	template_name= "productos/admin/editar.html"
	model = Productos
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")

class EliminarAdmin(LoginRequiredMixin,AdminRequiredMixins,DeleteView):
	template_name= "productos/admin/eliminar.html"
	model = Productos
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")


class Detalle(DetailView):
	template_name= "productos/detalle.html"
	model = Productos

class Listar(ListView):
	template_name= "productos/lista.html"
	model = Productos
	context_object_name= "productos"
	paginate_by=3


	def get_context_data(self, ** kwargs):
		context = super (Listar, self).get_context_data(** kwargs)
		context ["nombre_buscado"] = self.request.GET.get("nombre_producto","")
		return context

	def get_queryset(self):
		busqueda_nombre = self.request.GET.get("nombre_producto","")
		query = Productos.objects.all().order_by("nombre")
		if len(busqueda_nombre) > 0:
			query = query.filter(nombre__icontains=busqueda_nombre)
		return query 