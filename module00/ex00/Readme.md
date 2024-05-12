# Cross-Site Scripting (XSS)

## O que é?

Os ataques Cross-Site Scripting (XSS) são um tipo de injeção, na qual scripts maliciosos são injetados em de outra forma benigno e confiável sites. 

Os ataques XSS ocorrem quando um invasor usa um aplicativo da Web para enviar código malicioso, geralmente na forma de um script lateral do navegador, para um usuário final diferente. 

As falhas que permitem que esses ataques sejam bem-sucedidos são bastante difundida e ocorre em qualquer lugar que um aplicativo da web use a entrada de um usuário dentro da saída que gera sem validar ou codificar.

Um intruso pode utilizar o XSS para enviar um script malicioso para um suspeito desavisado usuário. O navegador do usuário final não tem como saber que o script deve não é confiável e executará o script. 

Porque ele pensa o O script veio de uma fonte confiável, o script malicioso pode acessar qualquer cookies, tokens de sessão ou outras informações sensíveis retidas pelo navegador e usado com esse site. 

Esses scripts podem até mesmo reescrever o Conteúdo da página HTML. Para mais detalhes sobre os diferentes tipos de XSS falhas, veja: Tipos de scripts entre sites.

___Fonte:___https://owasp.org/www-community/attacks/xss/

## Análise

### Explicação com base codigo fonte.

O script que lê o valor do campo input (inputText) não faz nenhuma consistência para validar se há algum código malicioso, tal como script, antes de criar o element script. Desse modo, toda vez que o usuário clicar no botão "Submit", o texto é injetado na integra dentro do "textContent" do script.

