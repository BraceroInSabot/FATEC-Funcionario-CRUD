from django.shortcuts import render
from django.views.generic import ListView

class ListarFuncionariosView(ListView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, 'index.html')