# Template Injection App

## O que é?

Os aplicativos da Web geralmente usam tecnologias de modelagem do lado do servidor (Jinja2, Twig, FreeMaker, etc.) para gerar respostas HTML dinâmicas.

As vulnerabilidades de injeção de modelo no servidor (SSTI) ocorrem quando a entrada do usuário é incorporada em um modelo de maneira insegura e resulta na execução remota de código no servidor. 

Quaisquer recursos que suportem marcação avançada fornecida pelo usuário podem ser vulneráveis ​​ao SSTI, incluindo páginas wiki, análises, aplicativos de marketing, sistemas CMS, etc. 

Alguns mecanismos de modelo empregam vários mecanismos (por exemplo, sandbox, lista de permissões, etc.) para proteção contra SSTI.

___Fonte:___ https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2---template-format

# Cenários

## Dados do servidor

Através de comandos, como "ls" e "cat", caso os dados informados não forem sanitizados, o atacante consegue listar arquivos e até mesmo exibir seus conteúdos.

## Negação de serviços

Com essa vulnerabilidade, o atacante pode inserir loops que venham minar recursos do servidor, tais como memória.

## Deleção de arquivos

Da mesma forma que o cenário de "dados do servidor", o atacante, pode até mesmo deletar arquivos do servidor, causando prejuizos e até mesmo afetando o negócio por trás da aplicação.