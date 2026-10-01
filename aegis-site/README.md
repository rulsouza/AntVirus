# AEGIS — Next-Gen Security

Site de vendas/apresentação do antivírus AEGIS, agora como aplicação **Flask** completa: cadastro e login com banco de dados, área interna, e fluxo de compra que abre em uma aba separada.

## Estrutura

```
aegis-site/
├── app.py                  # rotas da aplicação
├── database.py             # conexão e criação do banco SQLite
├── requirements.txt
├── static/
│   ├── css/style.css
│   └── img/logo.jpg
└── templates/
    ├── index.html          # landing page
    ├── login.html
    ├── cadastro.html
    ├── sistema.html         # área interna (protegida por sessão)
    ├── comprar.html         # checkout (abre em nova aba)
    └── comprar_sucesso.html
```

## Como rodar no VS Code

1. Abra a pasta `aegis-site` no VS Code.
2. Abra um terminal (**Terminal → New Terminal**) e crie o ambiente virtual:
   ```
   python -m venv .venv
   ```
3. Ative o ambiente:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
5. Rode o projeto:
   ```
   python app.py
   ```
6. Acesse **http://127.0.0.1:5000**

Na primeira execução o arquivo `database.db` e as tabelas `users` e `compras` são criados automaticamente.

## Como funciona

- **Cadastro/Login**: senha é armazenada com hash (`werkzeug.security`). Ao logar, a sessão Flask (`session["user_id"]`) guarda o usuário conectado.
- **Área interna (`/sistema`)**: só acessível logado; redireciona para `/login` caso contrário. Mostra as compras do usuário.
- **Comprar um plano**: nos planos pagos (Plus/Pro), se o usuário já está logado o botão abre `/comprar/<plano>` **em uma nova aba**. Se não está logado, primeiro cadastra a conta e já cai direto no checkout do plano escolhido.
- **Checkout (`/comprar/<plano>`)**: formulário simulado (sem gateway de pagamento real) que grava o pedido na tabela `compras` e mostra uma página de confirmação.
- **Botão "Analisar agora"**: chama `/api/scan`, que devolve um resultado simulado em JSON, e a página atualiza o painel via JavaScript (`fetch`).

## Próximos passos sugeridos

- Trocar o `app.secret_key` por uma chave segura antes de qualquer deploy real.
- Validar formato de e-mail e força de senha no cadastro.
- Adicionar recuperação de senha.
- Integrar um gateway de pagamento de verdade (Stripe, Mercado Pago, etc.) no checkout.
