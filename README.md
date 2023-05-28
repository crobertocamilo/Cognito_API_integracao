## Desafio 4 do ***Bootcamp Cloud* AWS**

Evento promovido pela [Digital Innovation One - DIO](https://www.dio.me/en), com patrocínio da [Amazon Web Services - AWS](https://aws.amazon.com/pt/).

<div align="right">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/logo_bootcamp.webp?raw=true.webp" alt="logo bootcamp" width=20%/>
</div>

--- 
## Desafio
**Adicionando Segurança em APIs na AWS com Amazon Cognito**

---
### Objetivo

Utilizar o AWS Cognito para oferecer autenticação, autorização e gerenciamento de usuários que acessam uma API.

* Utilizar os serviços Amazon Cognito, DynamoDB, API Gateway e AWS Lambda;
* Criar uma API REST no Amazon API Gateway;
* Criar tabela no Amazon DynamoDB;
* Criar funções no AWS Lambda;
* Integrar o API Gateway com o Lambda *backend*;
* Utilizar a ferramenta no POSTMAN;
* Criar um autorizador do Amazon Cognito para uma API REST no Amazon API Gateway.

---
### Desenvolvimento da solução:

A API utilizada neste projeto foi implementada utilizando o **Serverless Framework** e consiste na criação de uma tabela no **DynamoDB** e funções **Lambda**, integradas ao **API Gateway** para realizar operações sobre a tabela (inserir item, consultar, atualizar e deletar).

A criação de toda a infraestrutura da API é automática, e foi baseada no projeto que desenvolvi [neste repositório](https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python). Se desejar trocar o nome/tema da tabela, antes do *deploy*, renomeie o nome da tabela *Paises* e de sua chave *Pais*, no arquivo [serveless.yml](https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/serverless.yml) e nas funções python da pasta [src](https://github.com/crobertocamilo/Cognito_API_integracao/tree/main/src), para os nomes que desejar. 

---
### Implementando a solução:

Requisitos:
* Criar (ou possuir) uma conta na [AWS](https://aws.amazon.com/pt/);
* Serverless Framework instalado (tutorial oficial [aqui](https://www.serverless.com/framework/docs/tutorial));
* AWS-CLI [instalado](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) e configurado com as credenciais da conta (Access Key e Secret Key) na AWS. Para mais informações, clique [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/);
* Instalar o [**Postman**](https://www.postman.com/) para interação com as rotas da API.

<br></br>

Para realizar o *deploy* da API na AWS, clone este repositório e acesse a pasta raiz pelo terminal. Digite:

  `serverless deploy`

Se a estrutura de serviços for construída com sucesso em sua conta da AWS, será exibido no terminal uma mensagem como a mostrada abaixo, onde são listados os *endpoints* criados para cada método/operação no banco de dados. 

Os links mostrados na imagem são apenas exemplos e não estão mais disponíveis.

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/serverless_deploy.png?raw=true" alt="Estrutura de serviços na AWS" width=65%/>
</div>

<br></br>

A manipulação da tabela criada pode ser feita através do Postman, conforme exemplificado [aqui](https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python), mas respeitando o nome da chave primária (neste projeto, *"Pais"*). Como o DynamoDB é NoSQL, não é necessário que todos os registros da tabela tenham os mesmos atributos - o único campo obrigatório é a chave primária (*partition key*).

<br></br>
#### **> Criando um autenticador no AWS Cognito**

Para implementar autenticação e gerenciamento de usuários no acesso à API é possível criar um autenticador (*user pool*) no **Cognito**. O passo a passo está documentado neste pdf.

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/cognito_user_pool_criada.png?raw=true" alt="User pool criada no Cognito" width=65%/>
</div>

<div align="center">
User pool criada no Cognito.
</div>

<br></br>
#### **> Integrando o autenticador à API**

Em seguida, é necessário fazer a integração da *user pool* criada com a API criando um autorizador no API Gateway e o vinculando aos métodos que terão restrição de acesso, conforme exemplificado nas imagens abaixo:

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/integracao_api_gateway.png?raw=true" alt="Autorizador" width=55%/>
</div>

<div align="center">
Criando um autorizador no API Gateway.
</div>

<br></br>

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/integracao_api_gateway2.png?raw=true" alt="Vinculando o autorizador" width=56%/>
</div>

<div align="center">
Vinculando o autorizador ao método POST. Repetir para os outros métodos.
</div>

<br></br>

Com o autorizador vinculado, refaça o *deploy* da API clicando no botão *Actions*. A partir de então, o API Gateway não mais permitirá que um usuário insira novos dados na tabela, sendo necessário que ele se antes cadastre no Cognito.

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/post_bloqueado.png?raw=true" alt="Erro inserir item" width=56%/>
</div>

<div align="center">
Erro ao tentar inserir um item na tabela - Acesso bloqueado.
</div>

<br></br>
#### **> Acessando a API no Postman**

Para ter acesso novamente à API, é necessário gerar um *token* de acesso no Postan. A imagem abaixo mostra um exemplo de como os campos devem ser preenchidos os dados configurados na criação da *user pool* no Cognito. 

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/integracao_postman.png?raw=true" alt="Autorizador" width=55%/>
</div>

<div align="center">
Gerando um token para acesso à API no Postman.
</div>

<br></br>
#### **> Casdatrando um usário no Cognito**

Para concluir a geração do *token* de acesso, será necessário cadastrar um usuário no Cognito, informando um email e uma senha (os critério para a definição da senha foram definidos na criação da *user pool*), e em seguida confirmando o código de verificação recebido no email:

<table>
  <tr>
    <td>
      <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/cognito_login.png?raw=true" alt="Modificando registro 1" width="80%">
    </td>
    <td>
      <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/cognito_login2.png?raw=true" alt="Modificando registro 2" width="80%">
    </td>
  </tr>
</table>
<div align="center">
Cadastrando um usuário no Cognito e validando a conta.
</div>

<br></br>

Após o usuário ser validado, será concluída a geração do *token* no Postman. Copie o código gerado, e retorne à aba de POST em que a modificação na tabela havia sido bloqueada. Na seção *Autorization* da aba, selecione uma autenticação do tipo *OAuth 2.0" e cole o token gerado na etapa anterior:

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/postman_token.png?raw=true" alt="Configurando token" width=65%/>
</div>

<div align="center">
Configurando sua autorização no Postman.
</div>

<br></br>
Enfim, tente outra vez inserir um novo registro na tabela. Como agora você é um usário autorizado, o Cognito irá permitir o acesso à API e será possível realizar alterações na tabela!

<div align="center">
  <img src="https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/assets/post_autorizado.png?raw=true" alt="Autorizador" width=55%/>
</div>

<div align="center">
Novo registro inserido com sucesso na tabela.







