# API-DSM-ServiceDesk
<p align="center">
      <img src="/doc/front-end/logo-whatscode.svg" alt="logo da equipe" width="200">
      <h3 align="center"> WhatsCode | Equipe 3</h3>

<hr>

<p align="center">
  <a href ="#configuracoes"> Executando a aplicação </a>  | 
  <a href ="#planejamento"> Planejamento </a>  |
  <a href ="#mvp"> MVP </a>  |
  <a href ="#equipe"> Equipe </a> 
</p>

<h4 align="center">
 <a href="https://developer.mozilla.org/pt-BR/docs/Web/Guide/HTML/HTML5"><img src = "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/></a>
 <a href="https://developer.mozilla.org/pt-BR/docs/Web/CSS"><img src = "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/></a>
 <a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript"><img src = "https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/></a>
 <a href="https://www.python.org/"><img src ="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/></a>
 <a href="https://flask.palletsprojects.com/"><img src ="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/></a>
 <a href="https://www.mysql.com/"><img src ="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white"/></a>
 <a href="https://www.sqlalchemy.org/"><img src ="/doc/front-end/badge-sqlalchemy.svg" width="100"></a>
</h4>

<br>

> Status do Projeto: Em andamento 🕓

<br>


Em modo geral, uma Central de Serviços é uma ferramenta que presta assessoria para solucionar problemas integrado no ambiente de tecnologia da informação.
Este projeto será realizado baseado na metodologia ágil SCRUM, que foca no desenvolvimento da proatividade, autonomia e uma melhora da produtividade do time como um todo.

# Executando a aplicação <a id="configuracoes"></a>
Para a excução deste sistema temos disponibilado duas formas, com a instalação de um banco de dados local ou de um banco em nuvem. Caso a sua rede da máquina que está utilizando seja restrita é recomendado a instalação para o banco local. Caso contrário, pode-se pular as etapas da instalação do banco de dados e ir direto para os passos de Rodar a aplicação.

## Instalação do banco de dados
1. Ao clicar em `tag` aparecerá um arquivo *.zip* nominado v1.0.1 clique para baixá-lo.

2. 

3.
```
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bcda6317f670c5:56674bf3@us-cdbr-east-05.cleardb.net/heroku_041f3b642f4313b'
app.config['SQLALCHEMY_DATABASE_URI'] =
```

## Rodar a aplicação

1. Após a instalação, verifique se possui o Phyton já instalado em sua máquina. Apartir do comando no terminal: 
```
python --version
```
2. Caso não possua siga os passos de instalação do site oficial do Python: https://www.python.org/
3. Caso a resposta seja positiva, pelo terminal de sua preferência, se dirija até a pasta criada pelo arquivo *.zip*. 
```
cd <nome da pasta>
```
4. Vamos criar agora um ambiente virtual, pelo comando: 
```
py -3 -m venv venv
```
5. Criada, vamos ativa-la: 
```
.venv\Scripts\activate
```
6. Então, é só instalar o *requirements.txt*: 
```
pip install -r requirements.txt
```
Caso o comando acima não funcione, segue outra alternativa:
```
py -3 -m pip install -r requirements.txt
```
7. Certifique-se que está na pasta `src`, caso não esteja, retorne até a pasta principal utilizando o primeiro comando, e depois vá até a pasta
```
cd ..
cd src
```
8. Agora ainda no terminal, digite o seguinte código para começar a rodar o sistema:
```
flask run
```
9. Clique no link disponibilizado (com ctrl + clique). Pronto! Agora é só utilizar.


# Planejamento <a id="planejamento"></a>
Como mencionado no início deste documento o desenvolvimento do projeto foi baseado na metodologia SCRUM, que possui três principais pilares: transparência, inspeção e adaptação. Para êxito destes, é formulado um formato de entrega denominado sprint. Consistindo em um curto período para realizar tarefas determinadas que garantem entregas funcionais para o cliente. Neste momento, foi implementado a estrutura de três sprints com 21 dias cada: 

- Sprint 1 (25/03 - 14/04)
- Sprint 2 (25/04 - 15/05)
- Sprint 3 (16/05 - 05/06)

## Backlog do produto
Para uma melhor organização, o PO (Product Owner) da equipe maquetizou o backlog do produto, uma lista priorizada, refinada e estimada dos recursos que o time de desenvolvimento irá precisar para conseguir atingir o produto final desejado pelo cliente. O backlog foi pirorizados em alto, médio e baixo de acordo com o conversado com o cliente, em cima do valor de cada tópico. Na tabela, segue as tarefas ordenadas por prioridade, dividads pro sprints e mostrando ao lado o status de desenvolvimento de cada uma. 


| Tarefa                                        | Descrição                                                                                                                                                                                                                                      | Requisito     | Prioridade | Sprint | Status |
| :-------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: | :--------: | :----: | :----: |
| Layout no Figma                               | Criação de um layout final do projeto no Figma, para poder retirar prévias dúvidas com o cliente, onde estára em primeiro momento se adequando as necessidades do cliente. Para depois servir como base para o andamento do design do projeto. | Funcional     | Alta       | 1      | ✅ |
| Protótipo navegável                           | Começar a digitar os códigos em HTML e CSS para estruturação das páginas se baseando no layout proposto no Figma. Priorizando neste momento apenas as que irão ser utilizadas para a primeira entrega.                                         | Funcional     | Alta       | 1      | ✅ |
| Modelagem do banco de dados                   | Realizar o modelo conceitual e lógico no BrModelo, e a criação das tabelas no Workbench. Por ser uma modelagem incremental, o foco maior será no necessário para a funcionalidade desta primeira entrega.                                      | Não funcional | Alta       | 1      | ✅ |
| Banco de dados funcional                      | Através da modelagem do banco de dados feita anteriormente, precisará finalizar a estruração do mesmo.                                                                                                                                         | Não funcional | Alta       | 1      | ✅ |
| Ligação com o banco de dados | Utilizando o SQLAlchemy e Python para realizar a ligação das páginas feitas pela equipe do front-end | Não funcional | Alta | 1 | ✅|
| Relatório                                     | Uma das funcionalidades do administrador, em que realiza um cálculo percentual em cima das informaçõs das solcitações registradas do sistema.                                                                                                  | Funcional     | Alta       | 3      | 🕓 | 
| Distribuição da solicitação de serviços       | No momento em que a solicitação é registrada no sistema, esta deverá ser direcionada para algum executor de forma sequencial.                                                                                                                  | Funcional     | Alta       | 2      | 🕓 |
| Navegabilidade com Flask                      | Utilizar do mini framework Flask para realizar a navegabilidade entre as páginas do sistema.                                                                                                                                                   | Não funcional | Média      | 1      | ✅ |
| Vídeo do MVP                                  | Finalizando o desenvolvimento do MVP, algum menbro da equipe deverá gravar seu funcionamento e explicar tecnicamente os aspectos.                                                                                                              | Funcional     | Média      | 1      | ✅ |
| Documentação no github                        | Escrever descritivamente os passos realizados em cada entrega, realiza-lo de modo incremental a cada entrega.                                                                                                                                  | Não funcional | Média      | 1      | ✅ | 
| Usuário comum                                 | Determinar que este tipo de pessoa só poderá realizar solicaitações de serviços, verificar o seu histórico de envio e também avaliar a resposta do executor.                                                                                   | Funcional     | Média      | 2      | 🕓 | 
| Executor                                      | Na sua interface aparecerá apenas as solicitações encaminhadas para ele, e um filtro em que mostre os status de cada solicitação.                                                                                                              | Funcional     | Média      | 2      | 🕓 | 
| Administrador                                 | Será responsável por todo o sistema, então terá permissão de visualizar os históricos de solicitações (importante deixar filtro por executor), gerar relatórios e terá a permissão de tornar um usuário comum em executor ou vice versa.       | Funcional     | Média      | 2      | 🕓 | 
| Cadastro e login de usuários                  | Utilizando HTML, CSS e Python (ou JavaScript) será feito uma página para obter os dados do usuário e registra-lo no banco do sistema, no qual será determinante para definir as tarefas que poderão realizar na plataforma.                    | Funcional     | Baixa      | 2      | 🕓 | 
| Revisão e implementação do sistema            | Analisando as sugestões e orientações passadas nas entregas, revisar e/ou alterar pontos necessários do sistema.                                                                                                                               | Não funcional | Baixa      | 3      | 🕓 | 




## 1ª Sprint

O time se organizou para trazer um sistema simplificado do que foi pedido pelo cliente. Nesta versão, apresentaremos apenas as funcionalidades de envio de solicitação e armazenamento da mesma. Terá uma página do preenchimento da solicitação com o nome do cliente, tipo de serviço e a descrição do problema. Esta solicitação irá ser redirecionada para outra página onde será a visão do executor, pois neste ambiente ele poderá visualizar a solicitação e poderá dar um retorno.

### Front-end
Em primeiro momento foi realizado o layout do sistema na plataforma Figma, onde no desenvolvimento para esta primeira entrega foi focado apenas nas páginas que será exibidas. Sendo as páginas voltadas para um usuário comum (tela inicial do usuário, nova solicitação e histórico das solicitações) e as páginas para um executor (tela das demandas e resposta). O wireframe completo estará na pasta `doc/front-end` localizada neste repositório, abaixo está as imagens das páginas escolhidas:

<img src="/doc/front-end/wireframe-sprint1.png" alt="wireframe sprint 1" width="855" >
<img src="/doc/front-end/wireframe-sprint1(2).PNG" alt="wireframe sprint 1 (2)" width="855">

### Back-end
Paralelamente ao desenvolvimento das páginas, estava sendo modelado e preparado o banco de dados. Pensando em que a modelagem pode ser realizada através de implementaçãoes, priorizou-se apenas as criações das tabelas necessárias para o funcionamento do sistema nesta primeira entrega. Para tal, primeiramente realizaou-se os modelos conceitual e lógico.

**Modelo conceitual feito no brModelo.**
<img src="/doc/back-end/modeloConceitual-sprint1.jpg" alt="modelo conceitual sprint 1">

**Modelo lógico feito no Workbench.**
<img src="/doc/back-end/modeloLogico-sprint1.jpeg" alt="modelo lógico sprint 1">

Na sequência partiu-se para a criação do banco físico, utilizando a linguagem SQL na criação de tabelas. Segue imagens do momento da criação em que a linguagem DDL foi utilizada:
<img src="/doc/back-end/tabela1.jpg" alt="criação de tabelas">
<img src="/doc/back-end/tabela2.jpg" alt="criação de tabelas">

### Ligação com o banco de dados
Após estar finalizado a criação do banco de dados e já estar estruturado todas as páginas necessárias, realizou-se a ligação de ambas. Utilizando o mini framework Flask, linguagem Python e a biblioteca SQLAlchemy.

# MVP <a id="mvp"></a>
Mínimo produto viável (MVP) é uma versão funcional de modo enxuto do serviço inicialmente pensado. Onde uma pequena parcela de pessoas irá testar e experimenta-lo podendo assim opinar para futuras melhoras. Este conceito é implementado no SCRUM, onde geramos um MVP na primeira entrega e apartir dele continuamos implementando-o até chegar ao produto final.

Nosso MVP ficou da seguinte forma: 
![Animação1](https://user-images.githubusercontent.com/93659003/163466894-39f2c6d2-a105-47c0-898f-a6768a7e2360.gif)

Nós também realizamos um vídeo onde explicamos brevemente seu funcionamento e como conseguimos desenvolve-lo, segue o link: 
<a href="https://youtu.be/B5IebZFQw_Q">Link para acessar o vídeo</a>


      
      
      
      
# Equipe <a id="equipe"></a>

| Membro                | Função        | Github                                                                                                                                                | Linkedin                                                                                                                                                                                         |
| :-------------------: | :-----------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | 
| Thiago Oliveira       | Master        | <a href="https://github.com/ThiagoOAL"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>     | <a href="https://www.linkedin.com/in/thiagoleite042"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>                              |
| Mariana Kuroshima     | Product Owner | <a href="https://github.com/MariMiks"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>      | <a href="https://www.linkedin.com/in/mariana-izumi/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>                              |
| Jonatas Dallo         | Desenvolvedor | <a href="https://github.com/Jonatas-Dallo"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/jonatas-dall%C3%B3-147638206"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>                |
| Kevin Ribeiro         | Desenvolvedor | <a href="https://github.com/KevinRomRib"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>   | <a href="https://www.linkedin.com/in/kevinrribeiro/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>                              |
| Lucas Medici          | Desenvolvedor | <a href="https://github.com/LucasMedici"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>   | <a href="https://www.linkedin.com/in/lucas-medici-a15971237"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>                      |
| Matheus Augusto       | Desenvolvedor | <a href="https://github.com/MatheusAJesus"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/matheus-augusto-de-jesus-albernaz-918536216"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| Pedro Corrá           | Desenvolvedor | <a href="https://github.com/PHCorra"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>       | <a href="https://www.linkedin.com/in/pedro-c-95b57212a/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>                          |
