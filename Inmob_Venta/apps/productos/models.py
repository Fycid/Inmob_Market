from django.db import models
from apps.usuarios.models import Usuario

class Categorias(models.Model):
	nombre = models.CharField(max_length=250)


	class Meta:
		db_table:"Categorias"

	def __str__(self):
		return self.nombre

class Estado(models.Model):
	nombre = models.CharField(max_length=250)


	class Meta:
		db_table:"Estado"

	def __str__(self):
		return self.nombre

ESTADO_CHOICE= (
	(1, "En Venta"),
	(2, "Reservado"),
	(3,"Vendido"),
	(4, "En Alquiler"),
	(5, "Alquilado")

	)

class Productos(models.Model):
	nombre = models.CharField(max_length=250)
	precio = models.DecimalField(max_digits=10,decimal_places=2)
	detalle = models.TextField( default="")
	

	#Categorias = models.ManyToManyField(Categorias)#RELACION n A n
	Categorias = models.ForeignKey(Categorias,on_delete=models.CASCADE,null=True)#RELACION n A  1 
	
	usuario= models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
	#Estado = models.ForeignKey(Estado,on_delete=models.CASCADE,null=True)
	Estado = models.IntegerField(choices=ESTADO_CHOICE,default=1)
	imagen = models.ImageField(upload_to="productos", null=True)

	class Meta:
		db_table:"productos"
	
	def __str__(self):
		return self.nombre
	