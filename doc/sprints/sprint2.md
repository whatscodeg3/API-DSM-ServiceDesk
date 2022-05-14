# 2ª Sprint

PPara a segunda sprint, o time se organizou para implementar o MVP realizado na primeira parte do projeto. Funções como o cadastro/login de usuários, a implementação do administrador, opção para o executor de recusar uma solicitação, modo de atribuição cíclica das solicitações,possibilidade de adicionar arquivos no momento de abrir uma solicitação, usuário poderá avaliar a solução enviada pelo executor e para o administrador, foi implementado um relatório simples sem a adição de gráficos por hora. 

## Front-end
No front-end da segunda sprint planejamos terminar as telas restantes, ligando assim com o banco de dados. Segue abaixo o wireframe das páginas restantes feitas:

<img src="/doc/front-end/wireframe-sprint2.png" alt="wireframe sprint 1" width="855" >

## Back-end
Para o back-end, nós tivemos que alterar o banco de dados, adicionando a tabela avaliações e alterando a tabela usuários.

**Modelo lógico alterado.**
<img src="/doc/back-end/modelo-logico-2Sprint.jpeg" alt="modelo lógico sprint 1">

**DDL alterado.**

<img src="/doc/back-end/tabela1-2sprint.png" alt="criação de tabelas">
<img src="/doc/back-end/tabela1-2sprint.png" alt="criação de tabelas">
<img src="/doc/back-end/tabela1-2sprint.png" alt="criação de tabelas">

## Ligação com o banco de dados
Assim como na [primeira sprint](https://github.com/whatscodeg3/API-DSM-ServiceDesk/blob/main/doc/sprints/sprint1.md), nós realizamos a ligação das telas 
restantes com o banco de dados, utilizando o mini framework Flask, linguagem Python e a biblioteca SQLAlchemy.
