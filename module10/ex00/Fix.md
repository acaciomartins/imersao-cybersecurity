## Soluções

Podemos como prevenção ao ataque de "Template Injection App" sanitizar os dados enviados pela página para a aplicação de backend.

Abaixo 2 exemplos de código para sanitização de entrada do usuário.

### Exemplo #1:

```python
 user_input = request.form.get('input').replace("{", "").replace("}", "")
```

### Exemplo #2:

```python
    bad_chars = "'_#&;*}{"

    if any(char in bad_chars for char in user_input):
        abort(403)
```


_Fontes:_

- https://docs.cobalt.io/bestpractices/prevent-ssti/
- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
- https://www.paloaltonetworks.com/blog/prisma-cloud/template-injection-vulnerabilities/

