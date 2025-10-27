 # Instruções de uso:

1.  Faça um clone deste repositório:
```
	bash
    git clone https://github.com/RonaldoBittencourt/Python.git
```

2.  Suba os containers usando o Docker Compose.
```
	bash
    docker-compose up --build
```

### "O servidor estará rodando em 'http://localhost:8000/'."

# Decisões Técnicas:

1. Apps: O projeto foi estruturado em 2 apps principais: pedidos e produtos. Optei por essa separação para conseguir organizar melhor as funções.

2. Serializers: Nos serializers do pedido optei por separar os de leitura e os de escrita por questões de segurança a fim de evitar que o um usuário comum acabe enviando um campo mal intencionado ou algo parecido.

3. Imports: Fiz a importação de algumas bibliotecas e classes para resolver validações e problemas encontrados no caminho do projeto, como a validators e a decimal, que foram usadas para garantir que não fossem enviados produtos com preço negativo.

4. Segurança do banco: foi implementado algumas soluções de segurança e integridade para o banco, como o 'on_delete=PROTECT' no modelo de 'ItensPedido' para proteger um 'Produto' que tenha ligação com algum pedido já realizado seja excluído, o que garante uma integridade maior do histórico dos pedidos 

# Lista de Endpoints:

### Produtos:

* Listar produtos: **GET '/api/produtos/'**

* Criar produtos: **POST '/api/produtos/'**

* Detalhar produtos: **GET '/api/produtos/'id'/'**

* Atualizar produtos: **PATCH '/api/produtos/'id'/'**

* Deletar produtos: **DELETE '/api/produtos/'id'/'**

### Pedidos: 

* Listar pedidos: **GET '/api/pedidos/'**

* Criar pedidos: **POST '/api/pedidos/'**

* Listar com filtro de status: **GET '/api/pedidos/?status=PENDENTE'**

* Listar com filtro de email: **GET '/api/pedidos/?cliente_email=email@teste.com'**

* Listar com filtros combinados: **GET '/api/pedidos/?status=PAGO&cliente_email=email@teste.com'**

* Detalhar um pedido: **GET '/api/pedidos/'id'/'**

* Atualizar o status de um pedido (admin): **PATCH '/api/pedidos/'id'/status/'**

### Swagger:

* Baixar o schema: **'api/schema/'**

* Acessar o Swagger: **api/docs/**

* Acessar o Swagger simplificado: **api/redoc/**