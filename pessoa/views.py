from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario

class ListarFuncionariosView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Funcionario.objects.all()

    def get(self, request):
        return render(request, 'index.html', {'funcionarios': self.get_queryset()})