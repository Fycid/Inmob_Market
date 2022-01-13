from django.db import models

class Productos(models.Model):
	nombre = models.CharField(max_length=250)
	precio = models.DecimalField(max_digits=9,decimal_places=2)

	class Meta:
		db_table:"productos"

	def _str_(self):
		return self.nombre