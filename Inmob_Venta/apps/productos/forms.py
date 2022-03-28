from django import forms
from . models import Productos

class ProductoForm(forms.ModelForm):
	nombre = forms.CharField(label="Nombre del Producto",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ingrese el nombre del producto"}))
	detalle = forms.CharField(widget =forms.Textarea(attrs={"class":"form-control"}))
	class Meta:
		model = Productos
		fields = ["nombre","precio","detalle","Categorias","Estado","imagen"]
