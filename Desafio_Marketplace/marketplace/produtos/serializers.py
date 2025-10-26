# importando da framework os serializers e os models dos produtos
from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    # criando a classe meta que recebe esse nome por padrão 
    class Meta:
        model = Produto
        # sempre colocar o campo de ID pois o django cria um automaticamente
        fields = ['id', 'nome', 'preco', 'estoque', 'descricao']