Diante da posibilidade de inspecionar o código (F12), e sabendo que há um componente de output (```html <div id="output"></div>```), podemos inserir os camandos abaixo, e pelo retorno, exibir os dados em cookie.

Para reprodução, digite no campo de input os camando abaixo e clique no botão "Submit".

Comandos:

1) ```html document.getElementById("output").innerHTML = "Cookie.value: " + document.cookie; ```

2) ```html alert(document.cookie); ```

3) ```html console.log("Cookie.value: " + document.cookie); ```