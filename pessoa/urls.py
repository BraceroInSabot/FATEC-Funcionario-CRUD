from django.urls import path
from .views import ListarFuncionariosView

urlpatterns = [
    path("listar/", ListarFuncionariosView.as_view(), name="listar_pessoas"),
]