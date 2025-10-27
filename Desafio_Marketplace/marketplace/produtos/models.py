from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

# definindo a classe produto
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    estoque = models.PositiveIntegerField()
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    # usando metodo str para definir o retorno
    def __str__(self):
        return self.nome
    