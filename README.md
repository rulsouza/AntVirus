# Projeto-base Flask para Desenvolvimento de Sistemas

Uma base didática para começar projetos em grupo usando Python, Flask, templates Jinja2 e SQLite. O projeto traz cadastro, acesso simples e um CRUD de `records` somente como referência.

> Este material é introdutório: a tela de acesso não mantém uma sessão do usuário. Em projetos reais, autenticação deve ser implementada com cuidado.

## Preparação

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative no Linux/macOS:

```bash
source .venv/bin/activate
```

Ative no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python app.py
```

Depois, acesse: <http://127.0.0.1:5000>

Na primeira execução, o arquivo `database.db` e as tabelas `users` e `records` serão criados automaticamente.

## Organização

```text
app.py               cria a aplicação Flask e registra as rotas
config.py            configurações (SECRET_KEY)
database.py          conexão e criação das tabelas do SQLite
models/              um arquivo por entidade, com os SQLs (CRUD)
routes/              um arquivo por entidade, com as rotas (Blueprints)
templates/           páginas HTML com Jinja2 (uma subpasta por entidade)
static/css/          estilos da interface
```

Para criar uma entidade nova (ex.: `livros`): crie a tabela em `database.py`, o arquivo `models/livros.py` com os SQLs, o arquivo `routes/livros.py` com um Blueprint (registrado em `routes/__init__.py`) e a pasta `templates/livros/` com as páginas. Use `models/records.py` e `routes/records.py` como modelo. Nos templates, os endpoints levam o nome do Blueprint, como `url_for('livros.listar')`.

## O que você deverá modificar

1. Alterar o nome do sistema.
2. Alterar a descrição da página inicial.
3. Identificar a entidade principal do projeto.
4. Substituir ou adaptar o CRUD de `records`.
5. Criar os campos necessários.
6. Alterar o banco de dados.
7. Criar novas rotas.
8. Criar novos templates.
9. Implementar as funcionalidades específicas do projeto.
10. Melhorar a interface conforme necessário.

Por exemplo: uma biblioteca pode adaptar `records` para `livros`; uma clínica, para `pacientes`; uma oficina, para `veiculos`; e um estoque, para `produtos`.

## Próximos passos

* Adicionar uma nova tabela.
* Relacionar duas tabelas.
* Criar filtros e campo de busca.
* Criar uma página de detalhes.
* Validar campos e mostrar mensagens de erro.
* Melhorar a interface.
* Adicionar funcionalidades específicas do projeto.

---

## Semana do dia 28/09/2026

## Continuação do projeto — início do desenvolvimento

Na etapa anterior, cada grupo organizou o projeto no Trello e fez o fork do repositório padrão.

A partir de agora, o objetivo é começar a transformar o projeto-base em um sistema com identidade própria e relacionado ao tema escolhido por cada equipe.

Nesta etapa, ainda não é necessário implementar todas as funcionalidades do sistema.

O foco será:

- personalizar a página inicial;
- definir a identidade visual do projeto;
- organizar a navegação;
- preparar a primeira tela da área interna;
- começar a substituir os exemplos genéricos pelo contexto real do projeto.

---

## Objetivo da aula

Ao final da aula, o grupo deverá conseguir apresentar:

1. uma página inicial personalizada;
2. o nome e a proposta do sistema;
3. uma tela de acesso funcionando;
4. pelo menos uma tela da área interna;
5. uma estrutura inicial de navegação;
6. o planejamento da entidade principal do sistema.

A área interna ainda pode ser apenas visual.

O importante nesta etapa é que o projeto deixe de parecer o projeto-base e comece a representar o sistema que o grupo pretende desenvolver.

---

## 1. Antes de começar

Antes de realizar alterações, verifique se o projeto está funcionando corretamente.

Caso ainda seja necessário, prepare o ambiente:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

Antes de continuar, confirme que o projeto executa sem erros.

---

## 2. Personalizar a página inicial

A página inicial atual é apenas um exemplo.

Ela deverá ser transformada em uma **landing page do sistema desenvolvido pelo grupo**.

A landing page deve apresentar, no mínimo:

- nome do sistema;
- título ou chamada principal;
- breve descrição do projeto;
- problema que o sistema pretende resolver;
- público ou tipo de usuário que utilizará o sistema;
- botão para acessar o sistema.

Também deve ser criada uma identidade visual inicial.

Podem ser modificados:

- cores;
- fontes;
- botões;
- cards;
- espaçamento;
- imagens;
- ícones;
- organização das seções.

Não é necessário criar uma página muito grande.

Uma página simples, organizada e relacionada ao projeto é suficiente.

---

## 3. Preparar a área interna

O projeto-base possui a rota:

```text
/sistema
```

Essa página deverá começar a representar a área interna do projeto.

Por enquanto, ela **não precisa possuir funcionalidades completas**.

O objetivo é visualizar como o sistema será organizado.

Por exemplo:

### Biblioteca

A área interna poderia apresentar:

- Livros;
- Empréstimos;
- Usuários;
- Categorias.

### Clínica

A área interna poderia apresentar:

- Pacientes;
- Consultas;
- Profissionais;
- Agenda.

### Oficina

A área interna poderia apresentar:

- Veículos;
- Clientes;
- Ordens de Serviço;
- Serviços.

### Estoque

A área interna poderia apresentar:

- Produtos;
- Categorias;
- Entradas;
- Saídas;
- Relatórios.

Os links ou cards ainda podem não funcionar.

O importante é que a estrutura tenha relação com o projeto.

---

## 4. Criar uma navegação inicial

O usuário deverá conseguir navegar pelo sistema sem precisar digitar diretamente os endereços no navegador.

Verifique se existem caminhos para:

```text
Página inicial
      ↓
    Login
      ↓
Área interna
```

Podem ser utilizados:

- links;
- botões;
- menus;
- navbar;
- sidebar.

A estrutura ainda pode ser simples.

---

## 5. Identificar a entidade principal do projeto

O projeto-base possui um CRUD chamado:

```text
records
```

Ele existe apenas como exemplo.

Cada grupo deverá identificar qual será uma das principais entidades do próprio sistema.

Exemplos:

| Projeto | Entidade principal |
|---|---|
| Biblioteca | livros |
| Clínica | pacientes |
| Oficina | veículos |
| Estoque | produtos |
| Escola | alunos |
| Agenda | compromissos |

Pense também em quais dados essa entidade deverá possuir.

Exemplo:

### Livro

```text
título
autor
categoria
ano
disponível
```

### Paciente

```text
nome
telefone
data de nascimento
endereço
```

### Veículo

```text
placa
modelo
marca
ano
proprietário
```

Nesta aula, ainda não é obrigatório alterar todo o CRUD.

O grupo deverá, no mínimo, decidir qual será a entidade e registrar essa decisão no Trello.

---

## 6. Organização do trabalho em equipe

Evite que apenas uma pessoa do grupo desenvolva tudo.

Dividam as tarefas.

Uma possível divisão seria:

### Integrante 1

Landing page e conteúdo.

### Integrante 2

Identidade visual e CSS.

### Integrante 3

Área interna e navegação.

### Integrante 4

Organização do Trello, testes e revisão.

Essa divisão é apenas uma sugestão.

Cada equipe poderá organizar o trabalho da forma que considerar melhor.

---

## 7. Atualizar o Trello

Durante a aula, criem ou atualizem os cartões correspondentes às tarefas realizadas.

Exemplos:

```text
Criar landing page
```

```text
Definir identidade visual
```

```text
Personalizar tela interna
```

```text
Criar navegação
```

```text
Definir entidade principal
```

Ao concluir uma tarefa, mova o cartão para a coluna correspondente.

O Trello deverá representar o andamento real do projeto.

---

## 8. Fazer commits durante o desenvolvimento

Não deixem todas as alterações para um único commit no final da aula.

Sempre que uma parte importante for concluída, façam um commit.

Exemplos:

```bash
git add .
git commit -m "feat: personaliza landing page"
```

```bash
git commit -m "style: define identidade visual"
```

```bash
git commit -m "feat: cria estrutura inicial da area interna"
```

Ao final da aula:

```bash
git push
```

Certifique-se de que as alterações foram enviadas ao GitHub.

---

## 9. Sobre o login nesta etapa

O projeto-base já permite:

1. cadastrar um usuário;
2. armazenar a senha de forma protegida;
3. verificar o e-mail e a senha;
4. redirecionar o usuário para a área interna.

Por enquanto, isso será suficiente.

Ainda não é obrigatório implementar uma autenticação completa com sessão.

Atualmente, depois que o usuário informa corretamente seus dados, o sistema apenas redireciona para:

```text
/sistema
```

Nas próximas etapas, poderá ser implementada uma sessão para identificar o usuário que está conectado e impedir o acesso à área interna sem login.

---

## Desafio opcional — implementar sessão

Os grupos que terminarem a atividade principal poderão tentar implementar uma sessão simples.

Primeiro, importe:

```python
from flask import session
```

Depois que o usuário for identificado corretamente:

```python
session["user_id"] = user["id"]
```

Em uma rota interna:

```python
@app.route("/sistema")
def sistema():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("sistema.html")
```

Também pode ser criada uma rota para sair:

```python
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))
```

Com isso, o sistema passa a lembrar que o usuário realizou o login.

---

## 10. Checklist da aula

Antes de encerrar, confirme:

- [ ] o projeto executa sem erros;
- [ ] o sistema possui um nome próprio;
- [ ] a página inicial foi personalizada;
- [ ] a página inicial explica o objetivo do sistema;
- [ ] existe um botão para acessar o sistema;
- [ ] a tela de login funciona;
- [ ] existe uma área interna;
- [ ] a área interna possui conteúdo relacionado ao projeto;
- [ ] o grupo definiu uma entidade principal;
- [ ] as tarefas foram atualizadas no Trello;
- [ ] foram realizados commits;
- [ ] as alterações foram enviadas ao GitHub.

---

## Próximas etapas

Depois dessa estrutura inicial, o projeto deverá evoluir gradualmente.

As próximas etapas poderão incluir:

- substituir `records` pela entidade principal;
- alterar o banco SQLite;
- criar novos campos;
- criar formulários;
- implementar CRUD;
- relacionar tabelas;
- criar filtros;
- implementar busca;
- proteger rotas com sessão;
- mostrar informações do usuário conectado;
- validar dados;
- criar novas funcionalidades específicas de cada projeto.

O objetivo é que cada aula acrescente uma nova parte ao sistema até que o projeto-base seja completamente transformado no sistema desenvolvido pelo grupo.





