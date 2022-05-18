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
- Primeiramente, clique em `tag` e aparecerá um arquivo *.zip* nominado v1.0.1. Clique para baixá-lo.
- Para a excução deste sistema há duas formas: instalar um <a href="#instalar-banco">banco de dados local</a> ou utilizar um banco de dados na nuvem. Caso a sua rede seja restrita é recomendada a instalação de um banco local. Caso contrário, pode-se pular as etapas da instalação do banco de dados local e executar os passos de <a href="#rodar-app">Rodar a aplicação</a>.

## Instalação do banco de dados <a id="instalar-banco"></a>
### Banco de dados:
1. Execute o MySQL Workbench e selecione a conexão padrão 'Local instance MySQL80'

2. Execute o Script SQL abaixo:
```
CREATE DATABASE service;

USE service;

# Categoria dos usuarios e solicitações
CREATE TABLE IF NOT EXISTS categoria_usuarios (
	id_categoria_usuario INT NOT NULL AUTO_INCREMENT,
    categoria_usuario VARCHAR(45) NOT NULL,
    PRIMARY KEY(id_categoria_usuario)
);

CREATE TABLE IF NOT EXISTS categoria_solicitacoes (
	id_categoria_solicitacao INT NOT NULL AUTO_INCREMENT,
    categoria_solicitacao VARCHAR(45) NOT NULL UNIQUE,
    PRIMARY KEY(id_categoria_solicitacao)
);


# Inserindo valores em categoria usuarios e categoria solicitacoes
INSERT INTO categoria_usuarios(categoria_usuario) VALUES
("Usuário"),
("Executor"),
("Administrador");

INSERT INTO categoria_solicitacoes(categoria_solicitacao) VALUES
("Problema no Hardware"),
("Problema com Software"),
("Dúvidas/Esclarecimentos");

# Criando tabela de usuarios, avaliacoes e solicitacoes
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT ,
    nome_usuario VARCHAR(255) NOT NULL,
    email_usuario VARCHAR(255) NOT NULL UNIQUE,
    senha_usuario VARCHAR(14) NOT NULL,
    id_categoria_usuario INT,
    PRIMARY KEY (id_usuario),
    CONSTRAINT FK_id_categoria_usuario FOREIGN KEY (id_categoria_usuario)
    REFERENCES categoria_usuarios(id_categoria_usuario)
);
# Inserindo o Administrador em usuarios:
INSERT INTO usuarios (nome_usuario, email_usuario, senha_usuario, id_categoria_usuario) VALUES ('Administrador', 'admin@gmail.com', 'adm', 3);

CREATE TABLE IF NOT EXISTS avaliacoes (
	id_avaliacao INT NOT NULL AUTO_INCREMENT,
	descricao_avaliacao varchar(20),
    PRIMARY KEY (id_avaliacao)
);

# Inserindo valores em avaliacoes
INSERT INTO avaliacoes (descricao_avaliacao) VALUES ('Péssimo');
INSERT INTO avaliacoes (descricao_avaliacao) VALUES ('Regular');
INSERT INTO avaliacoes (descricao_avaliacao) VALUES ('Bom');
INSERT INTO avaliacoes (descricao_avaliacao) VALUES ('Ótimo');


CREATE TABLE IF NOT EXISTS solicitacoes(
	id_solicitacao INT NOT NULL AUTO_INCREMENT,
    data_abertura TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    data_aceite TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    data_fechamento TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    descricao_solicitacao TEXT NOT NULL,
    resposta_solicitacao TEXT,
    FK_id_usuario_comum INT,
    FK_id_executor INT,
    FK_id_categoria_usuario_comun INT,
    FK_id_categoria_executor INT,
    FK_id_categoria_solicitacao INT,
    FK_id_avaliacao INT,
    PRIMARY KEY(id_solicitacao),
    # Constraint categoria_usuario
    CONSTRAINT FK_id_categoria_usuario_solicitacao FOREIGN KEY (FK_id_categoria_usuario_comun)
    REFERENCES categoria_usuarios(id_categoria_usuario),
	CONSTRAINT FK_id_categoria_executor FOREIGN KEY (FK_id_categoria_executor)
    REFERENCES categoria_usuarios(id_categoria_usuario),
    # Constraint categoria_solicitacao
    CONSTRAINT FK_id_categoria_solicitacao FOREIGN KEY (FK_id_categoria_solicitacao)
    REFERENCES categoria_solicitacoes(id_categoria_solicitacao),
    # Constraint id_usuario_comum
    CONSTRAINT FK_id_usuario_comum FOREIGN KEY (FK_id_usuario_comum)
    REFERENCES usuarios(id_usuario),
    # Constraint id_executor
	CONSTRAINT FK_id_executor FOREIGN KEY (FK_id_executor)
    REFERENCES usuarios(id_usuario),
    # Constraint id_avaliacao
    CONSTRAINT FK_id_avaliacao FOREIGN KEY (FK_id_avaliacao)
    REFERENCES avaliacoes (id_avaliacao)
);

```
### IDE:
1. Descompacte o arquivo (projeto) baixado anteriormente.

2. Na sua IDE de preferência, abra o projeto denominado 'API-DSM-ServiceDesk'. 

3. Entre na pasta src e abra o arquivo app.py 

4. Comente a linha 7 desse arquivo (adicionando # no início da linha)
```
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bcda6317f670c5:56674bf3@us-cdbr-east-05.cleardb.net/heroku_041f3b642f4313b'

```
5. Descomente a linha 8 (retirando o # do início da linha) e altere apenas a palavra 'SENHA' para a senha que você usou para entrar na conexão padrão (passo 2).
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:SENHA@localhost/service'
```

## Rodar a aplicação <a id="rodar-app"></a>

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
.\venv\Scripts\activate
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
python index.py
```
9. Clique no link disponibilizado (com ctrl + clique). Pronto! Agora é só utilizar.


# Planejamento <a id="planejamento"></a>

Como mencionado no início deste documento o desenvolvimento do projeto foi baseado na metodologia SCRUM, que possui três principais pilares: transparência, inspeção e adaptação. Para êxito destes, é formulado um formato de entrega denominado sprint. Consistindo em um curto período para realizar tarefas determinadas que garantem entregas funcionais para o cliente. Neste momento, foi implementado a estrutura de três sprints com 21 dias cada. Abaixo está os links para vizualizar indivuidualmente o desenvolvimento de cada tópico:
- <a href='#sprints'>Sprints</a>
- <a href='#backlog'>Backlog do produto</a>
- <a href='#storys'>Histórias de usuário</a>

## Sprints <a id="sprints"></a>

- Sprint 1 (25/03 - 14/04): ([Link da Pasta](https://github.com/whatscodeg3/API-DSM-ServiceDesk/blob/main/doc/sprints/sprint1.md)): Concluído ✅
- Sprint 2 (25/04 - 15/05): ([Link da Pasta](https://github.com/whatscodeg3/API-DSM-ServiceDesk/blob/main/doc/sprints/sprint2.md)): Concluído ✅
- Sprint 3 (16/05 - 05/06): Carregando 🔋


## Backlog do produto <a id="backlog"></a>
Para uma melhor organização, o PO (Product Owner) da equipe maquetizou o backlog do produto, uma lista priorizada, refinada e estimada dos recursos que o time de desenvolvimento irá precisar para conseguir atingir o produto final desejado pelo cliente. O backlog foi pirorizados em alto, médio e baixo de acordo com o conversado com o cliente, em cima do valor de cada tópico. Na tabela, segue as tarefas ordenadas por prioridade, dividads pro sprints e mostrando ao lado o status de desenvolvimento de cada uma. 


| Tarefa                                        | Descrição                                                                                                                                                                                                                                      | Requisito     | Prioridade | Sprint | Status |
| :-------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: | :--------: | :----: | :----: |
| Layout no Figma                               | Criação de um layout final do projeto no Figma, para poder retirar prévias dúvidas com o cliente, onde estára em primeiro momento se adequando as necessidades do cliente. Para depois servir como base para o andamento do design do projeto. | Funcional     | Alta       | 1      | ✅ |
| Protótipo navegável                           | Começar a digitar os códigos em HTML e CSS para estruturação das páginas se baseando no layout proposto no Figma. Priorizando neste momento apenas as que irão ser utilizadas para a primeira entrega.                                         | Funcional     | Alta       | 1      | ✅ |
| Modelagem do banco de dados                   | Realizar o modelo conceitual e lógico no BrModelo, e a criação das tabelas no Workbench. Por ser uma modelagem incremental, o foco maior será no necessário para a funcionalidade desta primeira entrega.                                      | Não funcional | Alta       | 1      | ✅ |
| Banco de dados funcional                      | Através da modelagem do banco de dados feita anteriormente, precisará finalizar a estruração do mesmo.                                                                                                                                         | Não funcional | Alta       | 1      | ✅ |
| Ligação com o banco de dados                  | Utilizando o SQLAlchemy e Python para realizar a ligação das páginas feitas pela equipe do front-end | Não funcional | Alta | 1 | ✅|
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

## Histórias de usuário <a id="storys"></a>
O backlog mostrado anteriormente foi baseado nas histórias de usuário coletadas também pela PO da equipe. Nelas podemos observar exatamente o valor desejado pelo cliente e assim dividir as tarefas necessárias para o desenvolvimento da aplicação conforme o esperado e combinado.

<img src="/doc/historias-usuario.jpg" alt="tabela histórias de usuário">
Link para exibir a tabela com uma melhor visão da imagem acima <a href="/doc/historias-usuario.pdf">Tabela de história de usuários</a>



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
