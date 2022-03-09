from django import forms
from . models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
	#password = forms.CharField(widget=forms.PasswordInput())
	#nombre = forms.CharField(label="Nombre del Producto",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese el nombre del producto"}))


	class Meta:
		model = Usuario
		fields = ["username", "first_name","last_name","email" , "dni"]