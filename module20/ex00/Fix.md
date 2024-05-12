RCE - Execução de Código Remoto *(Remote Code Execution)*

Segue algumas dicas para minimizar a exposição a ataques e criar o software de maneira menos vulnerável desde o desenvolvimento.

A correção de uma vulnerabilidade como a RCE é basicamente a que acontece com outras vulnerabilidades da mesma categoria. 

Uma construção de código, validada e testada durante o seu período de construção, terá maiores chances de estar livre desse tipo de vulnerabilidade. 

### Sugestões de correções

1- Validação e Sanitização de entradas

Em relação a validação e sanitização, busque por caracteres especiais, símbolos e caracteres usados pela linguagem usada na aplicação bem como no sistema operacional que dá suporte à aplicação.

Como sugestão, também podemos gerar diversos tipos hashs combinando as mais variadas formas de serialização e encode, com por exemplo hash base64 com comandos serializados com pickle em Python)

2- WhiteList

Caso a aplicação necessite utilizar do recurso de executar algum comando no lado do servidor, recomenda-se a criação uma WhiteList seguindo o **Princípio do Menor Privilégio** onde só será liberado os comandos que de fato faça sentido ser executado no servidor.

3- Validação estático de código fonte

Utilizar de ferramentas para validação de código fonte para evitar a exposição de vulnerabilidades.



https://blog.convisoappsec.com/o-que-e-remote-code-execution/
https://github.com/videvelopers/Vulnerable-Flask-App
https://github.com/harsh-bothra/SecurityExplained/blob/main/resources/xxe-in-json.md
https://blog.convisoappsec.com/o-que-e-remote-code-execution/

uma abordagem Shift-Left