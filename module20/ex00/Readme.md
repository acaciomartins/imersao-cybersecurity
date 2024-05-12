# Vulnerable Flask App

## O que é?

Segundo a OWASP (Open Worldwide Application Security Project), é um ambiente de laboratório criado para pessoas que desejam se aprimorar na área de testes de penetração na web (Pentest).

### Vulnerabilidades envolvidas

Através desse laboratório é possível exercitar as habilidades nas seguintes vulnerabilidades:

- Injeção HTML
- XSS
- SSTI
- Injeção SQL
- Divulgação de informação
- Injeção de comando
- Força Bruta
- Desserialização
- Autenticação quebrada
- DOS
- Envio de arquivo


# RCE - Execução de Código Remoto *(Remote Code Execution)*

## O que é?

Remote Code Execution pode ser uma vulnerabilidade explorada do lado do servidor.

### Diferença entre XSS e RCE

RCE é diferente da vulnerabilidade XSS encontrada no OWASP Top 10, mesmo que está também seja uma vulnerabilidade onde há o uso de injeção de códigos.

A diferença básica é que o RCE é uma vulnerabilidade que explora uma fragilidade server-side, ou seja, o código enviado será executado do lado do servidor.

Já no XSS, por exemplo, o código utilizado explora uma fragilidade do lado do cliente, geralmente usando o browser do usuário para retornar com o dado ou a informação desejada.

### RCE

É a exploração de uma fragilidade na aplicação que permite que o atacante envie um código malicioso para ser executado.

Para isso, ele usa a linguagem da aplicação e a exploração executada em server-side.

Basicamente, qualquer aplicação que não tenha um tratamento adequado dos dados nela inseridos acabam sendo vulneráveis a este tipo de ataque.

Ilustração de um ataque RCE

![Alt text](image.png)

Para que possamos dizer que uma aplicação possa ser considerada vulnerável a RCE, duas condições básicas devem ser identificadas — ambas descritas de uma forma mais detalhada em CWE-94 e em CWE-95.

De forma geral, o CWE-94 descreve que, durante a construção de um software, este depende total ou parcialmente da introdução de dados.

No entanto, mesmo tendo a entrada de dados como parte fundamental do software, ele não realiza de forma adequada ações que possam neutralizar o uso arbitrário de códigos maliciosos.

Enquanto o CWE-94 fala sobre a necessidade de validar códigos e dados de entrada em um aplicativo, o CWE-95 trata da necessidade de tratamento de entradas das sintaxe de códigos antes delas serem processadas em uma chamada dinâmica (dynamic evaluation call).

Atacantes podem usar parâmetros de consulta para realizar ataques de RCE — ou ainda cookies ou o envio de arquivos para a aplicação.

### Como saber se a aplicação está vulnerável

![Alt text](image-2.png)

Através da inclusão, via Query String, o comando a ser executado no servidor. O exemplo abaixo, assim como na imagem, ilusta o uso do comando **phpinfo()** passasdo como parâmetro.

Url usada
```
http://localhost/rce/remotecode.php?code=phpinfo()
```



<br />
___Fontes:___

https://owasp.org/www-project-vulnerable-flask-app/
https://blog.convisoappsec.com/o-que-e-remote-code-execution/