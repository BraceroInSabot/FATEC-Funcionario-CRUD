from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Funcionario

class ListarFuncionariosView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Funcionario.objects.all()

    def get(self, request):
        return render(request, 'index.html', {'funcionarios': self.get_queryset()})

class CadastrarFuncionariosView(CreateView):
    template_name = 'templatesfuncionarioformulario.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        primeiroNome = request.POST.get('primeiroNome')
        segundoNome = request.POST.get('segundoNome')
        endereco = request.POST.get('endereco')
        sexo = request.POST.get('sexo')
        cpf = request.POST.get('cpf')
        dataNascimento = request.POST.get('dataNasc')
        telefone = request.POST.get('telefone')

        print(primeiroNome, segundoNome, endereco, sexo, cpf, dataNascimento, telefone)

        funcionario = Funcionario(
            primeiroNome=primeiroNome,
            segundoNome=segundoNome,
            endereco=endereco,
            sexo=sexo,
            cpf=cpf,
            dataNascimento=dataNascimento,
            telefone=telefone
        )
        funcionario.save()
        
        return render(request, 'index.html', {'funcionarios': Funcionario.objects.all()})   