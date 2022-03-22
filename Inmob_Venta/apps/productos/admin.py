from django.contrib import admin
from .models import Productos
from .models import Categorias
from .models import Estado


# Register your models here.

admin.site.register(Productos)
admin.site.register(Categorias)
admin.site.register(Estado)

