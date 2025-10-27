from rest_framework import generics
from .models import Pedido
from .serializers import (PedidoSerializer, PedidoCreateSerializer, PedidoStatusUpdateSerializer)

# Create your views here.

class PedidoListCreateView(generics.ListCreateAPIView):

    def get_queryset(self):
        # -data_criacao para ordenar do mais novo para o mais antigo
        queryset = Pedido.objects.all().order_by('-data_criacao')

        status = self.request.query_params.get('status')
        email_cliente = self.request.query_params.get('email_cliente')

        # verificando se os parâmetros necessários foram enviados
        if status:
            queryset = queryset.filter(status=status)

        # filtrando pelo email pois ele é único
        if email_cliente:
            queryset = queryset.filter(email_cliente=email_cliente)
            
        return queryset

    # função para decidir qual serializer usar
    def get_serializer_class(self):

        # POST para criação e GET para leitura
        if self.request.method == 'POST':
            return PedidoCreateSerializer
        else:
            return PedidoSerializer
        
# view para ver um pedido especifico
class PedidoRetrieveView(generics.RetrieveAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# view para atualizar o status do pedido
class PedidoStatusUpdateView(generics.UpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoStatusUpdateSerializer