# **Documentação do Aplicativo Urna-ETEC-LG**
**Nome provisório do projeto:** Urna-ETEC-LG

**Desenvolvedores:** Julio Basilio e Gabriel Menezes.
## **1. Objetivo do projeto**
O aplicativo **Urna-ETEC-LG** tem como objetivo facilitar o processo de escolha de candidatos, tornando a votação e o acesso às informações dos candidatos mais simples e acessíveis aos diferentes públicos.

Inicialmente, o aplicativo será destinado à eleição de um único representante de classe. Por esse motivo, a versão atual do sistema está sendo desenvolvida considerando apenas essa modalidade de votação, sem a necessidade de múltiplos cargos ou categorias de candidatos.

O projeto está sujeito a alterações ao longo de seu desenvolvimento, tanto em relação aos seus objetivos e funcionalidades quanto à sua interface visual e estrutura técnica.
## **2. Conceitos de programação utilizados**
### **2.1. Eleitores**
Os eleitores representam os usuários cadastrados no sistema que poderão participar da votação.

|**Atributo no banco de dados**|**Tipo de dado**|**Descrição**|
| :-: | :-: | :-: |
|id\_eleitor|INT|Identificador único do eleitor, gerado automaticamente pelo banco de dados.|
|rm\_eleitor|INT|Registro de matrícula do eleitor.|
|nome\_eleitor|VARCHAR(60)|Primeiro nome do eleitor.|
|sobreN\_eleitor|VARCHAR(60)|Sobrenome do eleitor.|
|idade\_eleitor|DATE|Data de nascimento do eleitor.|
|foto\_eleitor|VARCHAR(120)|Caminho ou endereço da foto do eleitor.|
|curso\_eleitor|VARCHAR(10)|Curso ao qual o eleitor pertence.|
### **2.2. Candidatos**
Os candidatos representam os alunos inscritos para concorrer à representação de classe.

|**Atributo no banco de dados**|**Tipo de dado**|**Descrição**|
| :-: | :-: | :-: |
|id\_cand|INT|Identificador único do candidato, gerado automaticamente.|
|id\_eleitor|INT|Identificador do eleitor associado ao candidato.|
|nome\_cand|VARCHAR(60)|Nome utilizado para identificar o candidato.|
|numero\_cand|INT|Número de identificação do candidato na votação.|
|foto\_cand|VARCHAR(120)|Caminho ou endereço da foto do candidato.|
|numerosVotos\_cand|INT|Campo destinado à quantidade de votos recebidos pelo candidato.|
### **2.3. Votos**
A tabela de votos armazena os registros das votações realizadas no sistema.

|**Atributo no banco de dados**|**Tipo de dado**|**Descrição**|
| :-: | :-: | :-: |
|id\_voto|INT|Identificador único do voto, gerado automaticamente.|
|id\_cand|INT|Identificador do candidato escolhido.|
|id\_eleitor|INT|Identificador do eleitor que realizou o voto.|
|dat\_voto|DATE|Data em que o voto foi registrado.|
### **2.4. Relacionamentos entre as tabelas**
O banco de dados utiliza chaves primárias e estrangeiras para relacionar os registros.

- **Eleitores e Candidatos:** a tabela Candidatos utiliza id\_eleitor como chave estrangeira para associar o candidato a um eleitor cadastrado.
- **Eleitores e Votos:** a tabela Votos utiliza id\_eleitor como chave estrangeira para identificar quem realizou o voto.
- **Candidatos e Votos:** a tabela Votos utiliza id\_cand como chave estrangeira para identificar o candidato escolhido.

Esses relacionamentos permitem associar os votos aos respectivos eleitores e candidatos.
## **3. Classe Conexao**
A classe Conexao, desenvolvida em Python, é responsável pela comunicação entre o sistema e o banco de dados MySQL chamado Urna.

Ela utiliza a biblioteca mysql.connector para estabelecer conexões, executar consultas SQL, cadastrar informações e registrar votos.
### **3.1. Atributos**

|**Atributo**|**Tipo**|**Descrição**|
| :-: | :-: | :-: |
|host|String|Endereço do servidor MySQL.|
|user|String|Nome do usuário utilizado para acessar o banco de dados.|
|password|String|Senha utilizada na autenticação do MySQL.|
|database|String|Nome do banco de dados utilizado pelo sistema.|
|conexao|Objeto de conexão|Armazena a conexão ativa com o banco de dados.|
|dadoPesquisa|Variável opcional|Armazena um valor de pesquisa fornecido durante a inicialização da classe.|
### **3.2. Métodos**

|**Método**|**Parâmetros**|**Descrição**|
| :-: | :-: | :-: |
|\_\_init\_\_()|dadoPesquisa (opcional)|Inicializa os atributos da classe e define as configurações de acesso ao banco de dados.|
|conectar()|Nenhum|Estabelece a conexão com o MySQL e retorna o objeto de conexão quando bem-sucedida.|
|fechar()|Nenhum|Encerra a conexão ativa com o banco de dados.|
|pesquisar()|tabela, dado, valor|Pesquisa registros em uma tabela e coluna permitidas, utilizando o valor informado como critério.|
|inserirEleitores()|rm, nome, sobrenome, idade, foto, curso|Insere um novo eleitor na tabela Eleitores.|
|inserirCandidato()|idEleitor, nomeCandidato, numeroCandidato, fotoCandidato|Cadastra um candidato associado a um eleitor existente.|
|inserirVotos()|idCand, idEleitor|Verifica se o eleitor já possui um voto registrado e, caso não possua, registra o voto com a data atual.|
### **3.3. Tratamento de erros**
Os métodos de acesso ao banco de dados utilizam estruturas try, except e finally para tratar possíveis erros durante as operações.

Quando ocorre um erro em uma operação de escrita, o sistema executa rollback() para desfazer as alterações não confirmadas. Quando a operação é concluída com sucesso, utiliza commit() para confirmar a gravação dos dados.

O fechamento dos cursores e das conexões é realizado para liberar os recursos utilizados.
### **3.4. Segurança e integridade dos votos**
A classe realiza uma consulta para verificar se o eleitor já possui um voto registrado antes de inserir um novo.

Para reforçar essa validação, o banco de dados deverá possuir uma restrição de unicidade sobre id\_eleitor na tabela Votos, garantindo que um eleitor não possa possuir mais de um registro de voto.

A integridade dos relacionamentos também é reforçada pelas chaves estrangeiras definidas no banco de dados.
## **4. Observações sobre o desenvolvimento**
A estrutura atual foi planejada para atender à eleição de um representante de classe. Novas funcionalidades poderão ser adicionadas conforme as necessidades do projeto e as decisões da equipe.

Os nomes, os tipos de dados, as funcionalidades e a interface do aplicativo poderão ser modificados durante o desenvolvimento, de acordo com os requisitos estabelecidos.

O projeto encontra-se em desenvolvimento, e as funcionalidades descritas serão submetidas a testes para verificar seu funcionamento e a integridade dos dados registrados.

