## 1ª Sprint

A equipe se organizou para trazer um sistema simplificado do que foi pedido pelo cliente. Nesta versão, apresentaremos apenas as funcionalidades de envio de solicitação e armazenamento da mesma. Terá uma página do preenchimento da solicitação com o nome do cliente, tipo de serviço e a descrição do problema. Esta solicitação irá ser redirecionada para outra página onde será a visão do executor, pois neste ambiente ele poderá visualizar a solicitação e poderá dar um retorno.

### Front-end
Em primeiro momento foi realizado o layout do sistema na plataforma Figma, onde no desenvolvimento para esta primeira entrega foi focado apenas nas páginas que será exibidas. Sendo as páginas voltadas para um usuário comum (tela inicial do usuário, nova solicitação e histórico das solicitações) e as páginas para um executor (tela das demandas e resposta). O wireframe completo estará na pasta `doc/front-end` localizada neste repositório, abaixo está as imagens das páginas escolhidas:

<img src="/doc/front-end/wireframe-sprint1.png" alt="wireframe sprint 1" width="855" >
<img src="/doc/front-end/wireframe-sprint1(2).PNG" alt="wireframe sprint 1 (2)" width="855">

### Back-end
Paralelamente ao desenvolvimento das páginas, estava sendo modelado e preparado o banco de dados. Pensando em que a modelagem pode ser realizada através de implementações, priorizou-se apenas as criações das tabelas necessárias para o funcionamento do sistema nesta primeira entrega. Para tal, primeiramente realizou-se o modelo conceitual e lógico.

**Modelo conceitual feito no brModelo.**
<img src="/doc/back-end/modeloConceitual-sprint1.jpg" alt="modelo conceitual sprint 1">

**Modelo lógico feito no Workbench.**
<img src="/doc/back-end/modeloLogico-sprint1.jpeg" alt="modelo lógico sprint 1">

Na sequência partiu-se para a criação do banco físico, utilizando a linguagem SQL na criação de tabelas. Segue imagens do momento da criação em que a linguagem DDL foi utilizada:
<img src="/doc/back-end/tabela1.jpg" alt="criação de tabelas">
<img src="/doc/back-end/tabela2.jpg" alt="criação de tabelas">

### Ligação com o banco de dados
Após estar finalizado a criação do banco de dados e já estar estruturado todas as páginas necessárias, realizou-se a ligação de ambas. Utilizando o mini framework Flask, linguagem Python e a biblioteca SQLAlchemy.
