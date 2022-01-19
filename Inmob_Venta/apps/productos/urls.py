from django.urls         import path
from .                   import views

app_name = "productos"

urlpatterns = [
    path('Detalle/', views.detalle, name = "detalle"),
    
    #admini
    path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
    path("Admin/nuevo/", views.NuevoAdmin.as_view(), name = "admin_nuevo")
]