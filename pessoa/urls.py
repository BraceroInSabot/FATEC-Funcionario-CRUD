from django.urls import path
from .views import ListarFuncionariosView, CadastrarFuncionariosView, EditarFuncionarioView

urlpatterns = [
    path("listar/", ListarFuncionariosView.as_view(), name="listar_funcionario"),
    path("cadastrar/", CadastrarFuncionariosView.as_view(), name="cadastrar_funcionario"),
    path("editar/<int:pk>", EditarFuncionarioView.as_view(), name="editar_funcionario"),
]