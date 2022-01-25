from django import forms
from . models import Productos

class ProductoForm(forms.ModelForm):
	nombre = forms.CharField(label="Nombre del Producto",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese el nombre del producto"}))
	class Meta:
		model = Productos
		fields = ["nombre","precio"]
