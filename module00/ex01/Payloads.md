Para os testes de vulnerabilidade, utilize os comandos abaixo:

### Payload 01

```sh
curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "amount=10" \
http://localhost:8080/transfer
```

### Payload 02

Através de uma página maliciosa, o usuário é induzido a clicar em um link que vai executar um comando de transferencia no valor de $1000, zerando a conta do usuário.

### Automacao

```sh
watch -n 60 \
curl -X POST \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "amount=10" \
http://localhost:8080/transfer
```