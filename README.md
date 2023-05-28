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
* Serverless Framework instalado (tutorial oficial [aqui](https://www.serverless.com/framework/docs/tutorial));
* AWS-CLI [instalado](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) e configurado com as credenciais da conta (Access Key e Secret Key) na AWS. Para mais informações, clique [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/).

<br></br>

---
### Implementando a solução:

Requisitos:
* Serverless Framework instalado (tutorial oficial [aqui](https://www.serverless.com/framework/docs/tutorial));
* AWS-CLI [instalado](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) e configurado com as credenciais da conta (Access Key e Secret Key) na AWS. Para mais informações, clique [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/).

<br></br>

Para o *deploy* deste projeto na AWS, clone este repositório e acesse a pasta raiz pelo terminal. Digite:

  `serverless deploy`

Se a estrutura de serviços for construída com sucesso em sua conta da AWS, será exibido no terminal uma mensagem como a mostrada abaixo, onde são listados os *endpoints* criados para cada método/operação no banco de dados. 

Os links mostrados na imagem são apenas exemplos e não estão mais disponíveis.

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/serverless_deploy.png?raw=true" alt="Estrutura de serviços na AWS" width=70%/>
</div>




