from django.db import models

# Create your models here.
ESTADOS = [
    ('PR', 'Paraná'),
    ('SP', 'São Paulo'),
    ('MG', 'Minas Gerais')
]
class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, choices=ESTADOS)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Qual o seu nome?", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name='Data de nascimento')
    email = models.EmailField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{}: {}'.format(self.nome, self.email)