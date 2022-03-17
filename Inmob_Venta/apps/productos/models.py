from django.db import models


class Categorias(models.Model):
	nombre = models.CharField(max_length=250)


	class Meta:
		db_table:"Categorias"

	def __str__(self):
		return self.nombre



class Productos(models.Model):
	nombre = models.CharField(max_length=250)
	precio = models.DecimalField(max_digits=10,decimal_places=2)
	detalle = models.CharField(max_length=250, null=True)

	#Categorias = models.ManyToManyField(Categorias)#RELACION n A n
	Categorias = models.ForeignKey(Categorias,on_delete=models.CASCADE,null=True)#RELACION n A  1 

	imagen = models.ImageField(upload_to="productos", null=True)

	class Meta:
		db_table:"productos"
	
	def __str__(self):
		return self.nombre
	