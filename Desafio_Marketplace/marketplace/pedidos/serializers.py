from rest_framework import serializers
from .models import Pedido, ItensPedido
from produtos.models import Produto

# um pedido deve:
#TODO: receber uma lista de produtos e quantidade
#TODO: verificar o preço de cada produto
#TODO: realizar o calculo do subtotal de cada item
#TODO: realizar o calculo do total de todo pedido
#TODO: verificar o estoque
#TODO: (opcional) atualizar o estoque ao confirmar o pedido
#TODO: ter o status atualizado pelo admin (outra view talvez)

# serializers para leitura
class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = ['id', 'produto', 'quantidade', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    # recebendo o serializer de cima para usar ele apenas para leitura
    itens = ItensPedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Pedido
        fields = [
            'id',
            'nome_cliente',
            'email_cliente',
            'data_criacao',
            'valor_total',
            'status',
            'itens'
        ]

# serializers de escrita
# serializer apenas para receber os dados do produto
class ItensPedidoWriteSerializer(serializers.Serializer):
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), source='produto')
    quantidade = serializers.IntegerField(min_value=1)

class PedidoCreateSerializer(serializers.ModelSerializer):
    # recebe o serializer de cima para criar um novo pedido
    itens = ItensPedidoWriteSerializer(many=True)
    class Meta:
        model = Pedido
        fields = ['nome_cliente', 'email_cliente', 'itens']
    
    # metodo para criar os pedidos
    #TODO: pensar em validação da quantidade do estoque antes de fazer o pedido
    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        # criando o pedido com o operador **
        pedido = Pedido.objects.create(**validated_data)
        valor_total_pedido = 0

        # criando loop para processar todos os dados
        for item_data in itens_data:
            produto = item_data['produto']
            quantidade = item_data['quantidade']

            subtotal = produto.preco * quantidade
            # incrementa o subtotal no valor total do pedido
            valor_total_pedido += subtotal

            # criando o objeto de cada item no banco
            ItensPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=quantidade,
                subtotal=subtotal
            )

            # atualizando o pedido com o calculo total do valor
            pedido.valor_total = valor_total_pedido
            pedido.save()
        return pedido
    
# serializer separado para mudar o status do pedido
# acessível apenas pelo admin
class PedidoStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['status']