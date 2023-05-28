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

A API utilizada neste projeto foi criada utilizando o **Serverless Framework** e consiste na criação de uma tabela no **DynamoDB** e funções **Lambda**, integradas ao **API Gateway** para realizar operações sobre a tabela (inserir item, consultar, atualizar e deletar).

Para fazer o *deploy* da API do projeto na AWS, clone este repositório e acesse a pasta raiz pelo terminal. Digite:

  `serverless deploy`

A criação de toda a infraestrutura da API é automática, e foi baseada no projeto que desenvolvi [neste repositório](https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python). Se desejar trocar o nome/tema da tabela, antes do *deploy*, renomeie o nome da tabela *Paises* e de sua chave *Pais*, no arquivo [serveless.yml](https://github.com/crobertocamilo/Cognito_API_integracao/blob/main/serverless.yml) e nas funções python da pasta [src](https://github.com/crobertocamilo/Cognito_API_integracao/tree/main/src), para os nomes que desejar.  



