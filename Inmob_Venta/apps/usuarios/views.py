from django.shortcuts           import render
from django.urls 				import reverse_lazy
from django.views.generic 		import ListView, CreateView
from django.contrib.auth.mixins	import LoginRequiredMixin
from apps.core.mixins 			import AdminRequiredMixins
from django.views.generic.edit 	import UpdateView, DeleteView
from django.urls 				import reverse_lazy


from  .forms 					import UsuarioForm
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
	


	
	def get_queryset(self):
		#self.request
		return Usuario.objects.all().order_by("id")

