from django.db import models

class Funcionario(models.Model):
    primeiroNome = models.CharField(max_length=100, verbose_name="Primeiro Nome", null=False, blank=False, db_column="PrimeiroNome")
    segundoNome = models.CharField(max_length=100, verbose_name="Ultimo Nome", null=False, blank=False, db_column="UltimoNome")
    endereco = models.CharField(max_length=200, verbose_name="Endereço", null=False, blank=False, db_column="Endereco")
    sexo = models.CharField(choices=(
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    ), max_length=10, verbose_name="Sexo", null=False, blank=False, db_column="Sexo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF", null=False, blank=False, db_column="CPF")
    dataNascimento = models.DateField(db_column="DataNascimento", verbose_name="Data de Nascimento", null=False, blank=False)
    telefone = models.CharField(max_length=15, verbose_name="Telefone", null=False, blank=False, db_column="Telefone")

    def __str__(self):
        return f"{self.primeiroNome} {self.segundoNome}"
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ['primeiroNome']