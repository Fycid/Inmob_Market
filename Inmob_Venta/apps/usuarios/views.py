from django.shortcuts           	import render
from django.urls 					import reverse_lazy
from django.views.generic 			import ListView, CreateView
from django.contrib.auth.mixins		import LoginRequiredMixin
from apps.core.mixins 				import AdminRequiredMixins
from django.views.generic.edit 		import UpdateView, DeleteView
from django.views.generic.detail 	import DetailView
from django.urls 					import reverse_lazy


from  .forms 					import UsuarioForm, UsuarioEdit
from  .models 					import Usuario


class Registrarme(CreateView):
	template_name= "usuarios/registrar.html"
	model = Usuario
	form_class = UsuarioForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("login")

class ListarUser(AdminRequiredMixins,LoginRequiredMixin,ListView):
	template_name = "usuarios/listar_us.html"
	model = Usuario
	context_object_name= "usuarios"
	paginate_by=2


	def get_queryset(self):
		#self.request
		return Usuario.objects.all().order_by("id")


class BorrarUser(LoginRequiredMixin,AdminRequiredMixins,DeleteView):
	template_name= "usuarios/eliminar_us.html"
	model = Usuario
	form_class = UsuarioForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("usuario:listar")

class EditarUser(LoginRequiredMixin,UpdateView):
	template_name= "usuarios/editar_us.html"
	model = Usuario
	form_class = UsuarioEdit
	
	def get_success_url(self, **kwargs):
		return reverse_lazy("usuario:listar")


class MiUser(LoginRequiredMixin,ListView):
	template_name = "usuarios/mi_us/mi_user.html"
	model = Usuario
	context_object_name= "usuarios"


	def get_queryset(self):
		self.request

class EditarMiUser(LoginRequiredMixin,UpdateView):
	template_name= "usuarios/mi_us/editar_mi_us.html"
	model = Usuario
	form_class = UsuarioEdit
	
	def get_success_url(self, **kwargs):
		return reverse_lazy("usuario:mi_usuario")
	