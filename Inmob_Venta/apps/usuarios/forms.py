from django import forms
from . models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
	
	username = forms.CharField(label="Usurario",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su nombre de usuario"}))
	first_name = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su nombre "}))
	last_name = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su Apellido "}))
	email = forms.CharField(label="Email",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su email "}))
	dni = forms.CharField(label="DNI",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese su DNI "}))

	#password = forms.CharField(widget=forms.PasswordInput())
	

	class Meta:
		model = Usuario
		fields = ["username", "first_name","last_name","email" , "dni"]