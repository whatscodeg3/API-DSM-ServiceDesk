# API-DSM-ServiceDesk
<p align="center">
      <img src="#" alt="logo da equipe" width="200" height="150">
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
</h4>

<br>

> Status do Projeto: Em andamento 🕓

<br>


Em modo geral, uma Central de Serviços é uma ferramenta que presta assessoria para solucionar problemas integrado no ambiente de tecnologia da informação.
Este projeto será realizado baseado na metodologia ágil SCRUM, que foca no desenvolvimento da proatividade, autonomia e uma melhora da produtividade do time como um todo.

# Configurações <a id="configuracoes"></a>
Para conseguir testar o sistema em qualquer local é necessário seguir o seguinte passo a passo:

Passo a passo:
-
-
-



# Planejamento <a id="planejamento"></a>
Como mencionado no início deste documento o desenvolvimento do projeto foi baseado na metodologia SCRUM, que possui três principais pilares: transparência, inspeção e adaptação. Para êxito destes, é formulado um formato de entrega denominado sprint. Consistindo em um curto período para realizar tarefas determinadas que garantem entregas funcionais para o cliente. Neste momento, foi implementado a estrutura de trÊs sprints com 21 dias cada: 

- Sprint 1 (25/03 - 14/04)
- Sprint 2 (25/04 - 15/05)
- Sprint 3 (16/05 - 05/06)

## Backlog do produto
Para uma melhor organização, o PO (Product Owner) da equipe maquetizou o backlog do produto, uma lista priorizada, refinada e estimada dos recursos que o time de desenvolvimento irá precisar para conseguir atingir o produto final desejado pelo cliente. O backlog foi pirorizados em alto, médio e baixo de acordo com o conversado com o cliente, em cima do valor de cada tópico. Na tabela, segue as tarefas ordenadas por prioridade, dividads pro sprints e mostrando ao lado o status de desenvolvimento de cada uma. 


| Tarefa                      | Descrição                                                                                                                                                                                                                                      | Requisito     | Prioridade | Status |
| :-------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: | :--------: | :---: |
| Layout no Figma             | Criação de um layout final do projeto no Figma, para poder retirar prévias dúvidas com o cliente, onde estára em primeiro momento se adequando as necessidades do cliente. Para depois servir como base para o andamento do design do projeto. | Funcional     | Alta       | ✅ |
| Protótipo navegável         | Começar a digitar os códigos em HTML e CSS para estruturação das páginas se baseando no layout proposto no Figma. Priorizando neste momento apenas as que irão ser utilizadas para a primeira entrega.                                         | Funcional     | Alta       | 🕓 |
| Modelagem do banco de dados | Realizar o modelo conceitual e lógico no BrModelo, e a criação das tabelas no Workbench. Por ser uma modelagem incremental, o foco maior será no necessário para a funcionalidade desta primeira entrega.                                      | Não funcional | Alta       | ✅ |
| Navegabilidade com Flask    | Utilizar do mini framework Flask para realizar a navegabilidade entre as páginas do sistema.                                                                                                                                                   | Não funcional | Média      | ✅ |


# 1ª Sprint

O time se organizou para trazer um sistema simplificado do que foi pedido pelo cliente. Nesta versão, apresentaremos apenas as funcionalidades de envio de solicitação e armazenamento da mesma. Terá uma página do preenchimento da solicitação com o nome do cliente, tipo de serviço e a descrição do problema. Esta solicitação irá ser redirecionada para outra página onde será a visão do executor, pois neste ambiente ele poderá visualizar a solicitação e poderá dar um retorno.

Em primeiro momento foi realizado o layout do sistema na plataforma Figma, onde no desenvolvimento para esta primeira entrega foi focado apenas nas páginas que será exibidas. Sendo as páginas voltadas para um usuário comum (tela inicial do usuário, nova solicitação e histórico das solicitações) e as páginas para um executor (tela das demandas e resposta). O wireframe completo estará na pasta `doc` localizada neste repositório, em seguida está as imagens das páginas escolhidas:

<img src="/doc/wireframe-sprint1.png" alt="wireframe sprint 1">
<img src="/doc/wireframe-sprint1(2).png" alt="wireframe sprint 1 (2)">

Paralelamente ao desenvolvimento das páginas, estava sendo modelado e preparado o banco de dados. Pensando em que a modelagem pode ser realizado através de implementaçãoes, priorizou-se apenas as criações das tabelas necessárias para o funcionamento do sistema nesta primeira entrega. Para tal, primeiramente realizaou-se os modelos conceitual e lógico.

Modelo conceitual feito no brModelo:
<img src="/doc/modeloConceitual-sprint1.jpg" alt="modelo conceitual sprint 1">

Modelo lógico feito no Workbench:
<img src="#" alt="modelo lógico sprint 1">

## MVP <a id="mvp"></a>


# Equipe <a id="equipe"></a>

| Membro                | Função        | Github                                                                                                                                                | Linkedin                                                                                                                  |
| :-------------------: | :-----------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------: | 
| Thiago Oliveira       | Master        | <a href="https://github.com/ThiagoOAL"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>     | <a href="https://www.linkedin.com/in/thiagoleite042"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| Mariana Kuroshima     | Product Owner | <a href="https://github.com/MariMiks"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>      | <a href="https://www.linkedin.com/in/mariana-izumi/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| Jonatas Dallo         | Desenvolvedor | <a href="https://github.com/Jonatas-Dallo"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/jonatas-dall%C3%B3-147638206"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| Kevin Ribeiro         | Desenvolvedor | <a href="https://github.com/KevinRomRib"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>   | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| Lucas Medici          | Desenvolvedor | <a href="https://github.com/LucasMedici"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>   | <a href="https://www.linkedin.com/in/lucas-medici-a15971237"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| Matheus Augusto       | Desenvolvedor | <a href="https://github.com/MatheusAJesus"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href="https://www.linkedin.com/in/matheus-augusto-de-jesus-albernaz-918536216"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
| Pedro Corrá           | Desenvolvedor | <a href="https://github.com/PHCorra"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>       | <a href="https://www.linkedin.com/in/pedro-c-95b57212a/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
