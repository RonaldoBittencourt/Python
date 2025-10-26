from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer

# Create your views here.

# criando a classe que vai herdar o ListCreateAPIView para o GET e POST
class ProdutoListCreateView(generics.ListCreateAPIView):
    # pegando todos os produtos
    queryset = Produto.objects.all()
    # definindo qual serializer vou usar
    serializer_class = ProdutoSerializer

# criando a classe que herda o RetrieveUpdateDestroyAPIView para o UPDATE E DELETE
class ProdutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


