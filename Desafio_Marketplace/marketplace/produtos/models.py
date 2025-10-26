from django.db import models

# Create your models here.

#TODO: verificar necessidade de testar erros de validação: ex preço negativo
# definindo a classe produto
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)

    # usando metodo str para definir o retorno
    def __str__(self):
        return self.nome
    