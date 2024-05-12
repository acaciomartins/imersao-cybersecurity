# Como prevenir vulnerabilidades XXE

Praticamente todas as vulnerabilidades XXE surgem porque a biblioteca de análise XML da aplicação suporta **recursos XML potencialmente perigosos** que a aplicação não precisa ou não nem pretende usar.

A versão 5+ já corrige a vulnerabilidade.

A maneira mais fácil e eficaz de prevenir ataques XXE é desabilitar esses recursos.

Na maioria das vezes, é suficiente desabilitar a resolução de entidades externas e desabilitar o suporte para XInclude. Isso geralmente pode ser feito por meio de opções de configuração ou substituindo programaticamente o comportamento padrão.

## Soluções

### Atualização de bibliotecas

Uma das recomendações é manter as bibliotecas sempre atualizadas. 

A biblioteca "lxml" é a biblioteca que faz o parse do xml, por esse motivo, manter essa biblioteca atualizada é primordial.

### Desabilitar a Resolução de Entidade

**Python**

**Vulnerabilidade**

Verificar se o uso da função **XMLParser**, está passando o parâmetro **resolve_entities** com valor **True**.

```Python
parser = etree.XMLParser(no_network=False, resolve_entities=True)
```

Como solução, pode-se remover o parâmetro, passando apenas o **no_netwrok**, ou, continuar enviando o parâmetro **resolve_entities** porém com valor **False**.

Exemplo:


**Com vulnerabilidade**
```python
parser = etree.XMLParser(no_network=False, resolve_entities=True)
```

**Com correção**
```python
parser = etree.XMLParser(no_network=False)
```
ou
```python
parser = etree.XMLParser(no_network=False, resolve_entities=False)
```