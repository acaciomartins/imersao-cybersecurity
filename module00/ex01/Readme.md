# CSRF (Cross site request forgery)

## O que é?

CSRF é um ataque que engana a vítima para que envie uma solicitação maliciosa. Ele herda a identidade e os privilégios da vítima para executar uma função indesejada em nome da vítima (embora observe que isso não é verdade para o login CSRF, uma forma especial de ataque descrita abaixo). Para a maioria dos sites, as solicitações do navegador incluem automaticamente quaisquer credenciais associadas ao site, como cookie de sessão do usuário, endereço IP, credenciais de domínio do Windows e assim por diante. Portanto, se o usuário estiver atualmente autenticado no site, o site não terá como distinguir entre a solicitação forjada enviada pela vítima e uma solicitação legítima enviada pela vítima.

Os ataques CSRF têm como alvo funcionalidades que causam uma mudança de estado no servidor, como alterar o endereço de e-mail ou senha da vítima, ou comprar algo. Forçar a vítima a recuperar dados não beneficia o invasor porque o invasor não recebe a resposta, mas a vítima. Como tal, os ataques CSRF têm como alvo solicitações de mudança de estado.

Um invasor pode usar CSRF para obter os dados privados da vítima por meio de uma forma especial de ataque, conhecida como login CSRF. O invasor força um usuário não autenticado a fazer login em uma conta controlada pelo invasor. Se a vítima não perceber isso, poderá adicionar dados pessoais – como informações de cartão de crédito – à conta. O invasor pode então fazer login novamente na conta para visualizar esses dados, juntamente com o histórico de atividades da vítima no aplicativo web.

Às vezes é possível armazenar o ataque CSRF no próprio site vulnerável. Essas vulnerabilidades são chamadas de “falhas de CSRF armazenadas”. Isso pode ser feito simplesmente armazenando uma tag IMG ou IFRAME em um campo que aceita HTML ou por meio de um ataque de script entre sites mais complexo. Se o ataque puder armazenar um ataque CSRF no site, a gravidade do ataque será amplificada. Em particular, a probabilidade aumenta porque é mais provável que a vítima visualize a página que contém o ataque do que alguma página aleatória na Internet. A probabilidade também aumenta porque a vítima já está autenticada no site.

## Sinônimos
Os ataques CSRF também são conhecidos por vários outros nomes, incluindo XSRF, “Sea Surf”, Session Riding, Cross-Site Reference Forgery e Hostile Linking. A Microsoft se refere a esse tipo de ataque como ataque de um clique em seu processo de modelagem de ameaças e em muitos lugares de sua documentação online.

___Fonte:___ https://owasp.org/www-community/attacks/csrf

# Cenários

## E-commerce

Após o usuário se autenticar, e caso o backend não possua um controle de acesso mais apurado, o atacante pode enviar, de forma maliciosa, um link induzindo a vítima a realizar uma compra indesejada.

## Notícias falsas (fake news)

Atacantes maliciosos, podem, induzir a vítima, através de um clique, enviar notícias manipuladas pelo atacante.

## Uso do XSS + CSRF

O atacante, pelo XSS pode incluir um código malicioso na página vulnerável a XSS, para que a mesma, utilize do acesso do usuário e execute o CSRF.