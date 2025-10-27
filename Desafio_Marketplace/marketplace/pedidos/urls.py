from django.urls import path
from . import views

urlpatterns = [
    # URL para o GET e o POST
    path('pedidos/', views.PedidoListCreateView.as_view(), name='pedido-list-create'),

    # URL para o GET
    path('pedidos/<int:pk>/', views.PedidoRetrieveView.as_view(), name='pedido-detail'),

    # URL para o PATCH
    path('pedidos/<int:pk>/status/', views.PedidoStatusUpdateView.as_view(), name='pedido-status-update'),
]