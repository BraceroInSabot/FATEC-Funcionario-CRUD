from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
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
    
class EditarFuncionarioView(UpdateView):
    template_name = 'templateFuncEditar.html'

    def get(self, request, pk):
        funcionario = Funcionario.objects.get(pk=pk)
        return render(request, self.template_name, {'funcionario': funcionario})
    
    def post(self, request, *args, **kwargs):
        funcionario = Funcionario.objects.get(pk=kwargs['pk'])
        funcionario.primeiroNome = request.POST.get('primeiroNome')
        funcionario.segundoNome = request.POST.get('segundoNome')
        funcionario.endereco = request.POST.get('endereco')
        funcionario.sexo = request.POST.get('sexo')
        funcionario.cpf = request.POST.get('cpf')
        funcionario.dataNascimento = request.POST.get('dataNasc')
        funcionario.telefone = request.POST.get('telefone')

        funcionario.save()
        
        return redirect('listar_funcionario')