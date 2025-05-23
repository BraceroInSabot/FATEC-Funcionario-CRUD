# Generated by Django 5.2 on 2025-05-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "primeiroNome",
                    models.CharField(
                        db_column="PrimeiroNome",
                        max_length=100,
                        verbose_name="Primeiro Nome",
                    ),
                ),
                (
                    "segundoNome",
                    models.CharField(
                        db_column="UltimoNome",
                        max_length=100,
                        verbose_name="Ultimo Nome",
                    ),
                ),
                (
                    "endereco",
                    models.CharField(
                        db_column="Endereco", max_length=200, verbose_name="Endereço"
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        choices=[("Masculino", "Masculino"), ("Feminino", "Feminino")],
                        db_column="Sexo",
                        max_length=10,
                        verbose_name="Sexo",
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        db_column="CPF", max_length=14, unique=True, verbose_name="CPF"
                    ),
                ),
                (
                    "dataNascimento",
                    models.DateField(
                        db_column="DataNascimento", verbose_name="Data de Nascimento"
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        db_column="Telefone", max_length=15, verbose_name="Telefone"
                    ),
                ),
            ],
            options={
                "verbose_name": "Funcionário",
                "verbose_name_plural": "Funcionários",
                "ordering": ["primeiroNome"],
            },
        ),
    ]
