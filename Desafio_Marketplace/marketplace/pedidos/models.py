from django.db import models
from produtos.models import Produto

# Create your models here.

class Pedido(models.Model):
    Status_opcoes = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('ENVIADO', 'Enviado'),
        ('CANCELADO', 'Cancelado'),
    ]

    # campos dos clientes
    #TODO:criar um app só para os clientes quando for fazer a autenticação
    nome_cliente = models.CharField(max_length=255)
    email_cliente = models.EmailField()

    # campos dos pedidos
    data_criacao = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, choices=Status_opcoes, default='PENDENTE')


    def __str__(self):
        return f"Pedido {self.id} - {self.nome_cliente}"

# definindo a classe dos itens dos pedidos para linkar essa tabela com a tabela de produtos
class ItensPedido(models.Model):

    # definindo o pedido como uma chave estrangeira
    # usando o CASCADE para excluir do banco todos os itens do pedido e não apenas um
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    # usando o PROTECT para proteger a classe parent ao deletar
    #TODO: verificar sobre o models.PROTECT q não funcionou como deveria
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido {self.pedido.id})"
    