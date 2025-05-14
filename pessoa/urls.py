from django.urls import path
from .views import ListarFuncionariosView, CadastrarFuncionariosView

urlpatterns = [
    path("listar/", ListarFuncionariosView.as_view(), name="listar_funcionario"),
    path("cadastrar/", CadastrarFuncionariosView.as_view(), name="cadastrar_funcionario"),
]