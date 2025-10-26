from django.urls import path
from . import views

urlpatterns = [
    # URL para o GET e o POST
    # .as_view() é obrigatório pra trabalhar com a classe View
    path('produtos/', views.ProdutoListCreateView.as_view(), name='produto-list-create'),

    # URL para o UPDATE e DELETE
    # utilizando o <int:pk> para pegar o numero inteiro (ID) e usar como primary key
    path('produtos/<int:pk>/', views.ProdutoRetrieveUpdateDestroyView.as_view(), name='produto-detail'),
];