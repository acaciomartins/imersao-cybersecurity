
# O que é XML external entity (XXE) injection

## Quais são os tipos de ataques XXE?

Existem vários tipos de ataques XXE:

- **Explorando XXE para recuperar arquivos**, onde é definida uma entidade externa contendo o conteúdo de um arquivo, e retornada na resposta da aplicação.

- **Explorando XXE para realizar ataques SSRF**, onde uma entidade externa é definida com base em uma URL para um sistema back-end.

- Exploração de dados de exfiltração cego XXE fora de banda , onde dados confidenciais são transmitidos do servidor de aplicativos para um sistema que o invasor controla.

- Explorando o blind XXE *(Vulnerabilidades cegas)*, para recuperar dados por meio de mensagens de erro , onde o invasor pode acionar uma mensagem de erro de análise contendo dados confidenciais.


## Explorando XXE para recuperar arquivos

Segue abaixo as instruções para exploração do vulnerabilidade onde o invasor vai recuperar dados de um arquivo no servidor.

Para realizar um ataque de injeção XXE que recupera um arquivo arbitrário do sistema de arquivos do servidor, é necessário modificar o XML enviado de duas maneiras:

- Introduza (ou edite) um DOCTYPEelemento que defina uma entidade externa contendo o caminho para o arquivo.

- Edite um valor de dados no XML que é retornado na resposta do aplicativo, para utilizar a entidade externa definida.


Por exemplo, suponha que um aplicativo de compras verifique o nível de estoque de um produto enviando o seguinte XML ao servidor:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>381</productId></stockCheck>
```

O aplicativo não executa nenhuma defesa específica contra ataques XXE, portanto, você pode explorar a vulnerabilidade XXE para recuperar o /etc/passwdarquivo enviando a seguinte carga XXE:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```

Esta carga XXE define uma entidade externa &xxe;cujo valor é o conteúdo do /etc/passwdarquivo e usa a entidade dentro do productIdvalor. Isso faz com que a resposta do aplicativo inclua o conteúdo do arquivo:

```
Invalid product ID: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
```

> **Observação**
>
>Com vulnerabilidades XXE do mundo real, muitas vezes haverá um grande número de valores de dados no XML enviado, qualquer um dos quais poderá ser usado na resposta do aplicativo. Para testar sistematicamente as vulnerabilidades XXE, geralmente você precisará testar cada nó de dados no XML individualmente, fazendo uso de sua entidade definida e verificando se ela aparece na resposta.


___Fontes:___ 
- https://portswigger.net/web-security/xxe
- https://github.com/payloadbox/xxe-injection-payload-list?tab=readme-ov-file
- https://portswigger.net/web-security/all-labs#xml-external-entity-xxe-injection (Laboratório)