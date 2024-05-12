## Soluções

### Solução 01

- Remover as linhas que fazem a inclusão do script.

Linhas a serem removidas.

```
    var script = document.createElement("script");

    script.textContent = userInput;

    document.body.appendChild(script);
```

### Solução 02

Concatenar nos dados inputado pelo usuário o caracter "'"

Ex.:

```
script.textContent = "'" + userInput + "'";
```


### Solução 03

Caso, a inclusão de script pelo usuário seja um requisito, podemos criar uma black list relacionando os scripts proibidos:

Ex.:

Black list (comandos a serem ignorados)

- document.cookie


### Solução 04

## Realizar escape nos dados de input.

Ex.:

```
function escape(element) {
    var res, html = element.value;
    res = html.replace(/<script.*<\/script>/g, "");
    return res;
}
```

Consumo:

```
var userInput = escape(document.getElementById("inputText"));
```

