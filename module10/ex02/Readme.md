# SSRF - Server-Side Request Forgery

## O que é SSRF?

SSRF é um vetor de ataque que abusa de uma aplicação para interagir com a rede interna/externa ou com a própria máquina.

Um dos facilitadores desse vetor é o manuseio incorreto de URLs.

### Visão geral de um fluxo comum SSRF

![MarineGEO circle logo](https://cheatsheetseries.owasp.org/assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Common_Flow.png "MarineGEO logo")

> **Observações**
> - SSRF não está limitado apenas ao protocolo HTTP. **Geralmente, a primeira solicitação é HTTP**, mas nos casos em que a própria aplicação realiza a segunda solicitação, ela pode usar diferentes protocolos, como por exemplo protocolos **FTP, SMB, SMTP, etc.,** e esquemas (schemes), como por exemplo **file://, phar://, gopher://, data://, dict://, etc.**.
>
> - Se o aplicativo for vulnerável à **injeção de XML eXternal Entity (XXE)** ele poderá ser explorado para realizar um ataque SSRF.


### Cenários

Dependendo da funcionalidade e dos requisitos da aplicação, existem dois casos básicos em que o SSRF pode acontecer.

#### Cenário 01 - Acessos aplicações internas

A requisição pode enviar solicitações apenas para aplicações **identificados e confiáveis**: caso em que a abordagem de lista de permissões está disponível, barrando acesso a qualquer aplicação.

Um exemplo nesse cenário é o acesso há recursos da AWS como DynamoDB onde o acesso é exposto via url interna.

Em ambientes de nuvem, o SSRF é frequentemente usado para acessar e roubar credenciais e tokens de acesso de serviços de metadados (AWS Instance Metadata Service, Azure Instance Metadata Service, servidor de metadados GCP).

#### Cenário 02 - Leitura de arquivos

A requisição pode enviar solicitações apenas para aplicações **identificados e confiáveis**: caso em que a abordagem de lista de permissões está disponível, barrando acesso a qualquer aplicação.

#### Cenário 03 - Acessos aplicações externas

A requisição pode enviar solicitações para **QUALQUER endereço IP externo ou nome de domínio**: Caso a abordagem da lista de permissões não esteja disponível.


## O que é LFI

**LFI (Local File Inclusion)** é uma vulnerabilidade de segurança da informação que pode ser explorado para obter acesso a sistemas e redes de computadores.
LFI significa Inclusão de Arquivos Locais e pode ter sérias consequências se não for tratado corretamente.

A vulnerabilidade de LFI ocorre quando um aplicativo da web permite que um usuário acesse arquivos locais do servidor sem a devida autorização.

Por exemplo, se um aplicativo da web permite que um usuário acesse um arquivo que está armazenado no servidor, mas não verifica se o usuário tem permissão para acessar esse arquivo, então isso pode levar a uma vulnerabilidade de LFI.

Isso pode permitir que um invasor acesse arquivos sensíveis, como senhas de banco de dados ou arquivos de configuração, e até execute código malicioso no servidor.

<br/>

_Fontes:_

- https://owasp.org/www-community/attacks/Server_Side_Request_Forgery
- https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html


