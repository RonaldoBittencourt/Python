#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#TODO: entender como django funciona
#TODO: definir como separar em aps as partes do projeto
#TODO: CRUD de produtos (nome, preco, estoque, descricao)
#TODO: CRUD de pedidos (cliente(nome, email), itens(produto, quantidade, subtotal), valor total, status)
#TODO: endpoint para o admin atulizar o status do pedido
#TODO: filtro de status do pedido e por clientes
#TODO: criar uma seed inicial
#TODO: entender e configurar docker para o projeto
#TODO: verificar objetivos adicionais para o desafio