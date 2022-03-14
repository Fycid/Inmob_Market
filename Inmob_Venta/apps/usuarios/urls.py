from django.urls         import path
from .                   import views

app_name = "usuario"

urlpatterns = [
    path('Registrarme/', views.Registrarme.as_view(), name = "registrarme"),
    path('Usuarios/Listar_us/', views.ListarUser.as_view(), name = "listar"),
    

  

]