# Soluções para vulnerabilidade de SSRF

Várias medidas de proteção são possíveis nas camadas de Aplicação e Rede.  Para aplicar o **Princípio da Defesa em Profundidade** *(Defense in Depth)*, ambas as camadas serão reforçadas contra tais ataques.

### Camada de Aplicação

#### Validação dos dados de entrada

- Validar se as entradas (literais, IPs, domínios e URL) estão presente em alguma blacklist contendo acessos restritos que serão impedidos na requisição.

- Validar via regex entradas simples, tais como: token, etc..

**Exemplo de código**

```JavaScript
import re
from flask import abort

//Regex validation for a data having a simple format

patternInput = "[a-zA-Z0-9\\s\\-]{1,50}"
matchedInput = re.search(patternInput, userInput)

if matchedInput:
    // Rejeita a requisição e não da continuidade na aplicação
    print('Vulnerabilidade encontrada. Requisição contêm dados da blacklist!')
    abort(403)
else:
    // Continua o processamento porque os dados enviados na requisição são válidos.
     
```

### Validações usando bibliotecas

#### Validações de IPs

> **Java:** InetAddressValidator.isValid (Apache Commons Validator)
>
> **.Net:** IPAddress.TryParse (SDK)
>
> **JavaScript:** ip-address
>
> **Ruby:** IPAddr (SDK)

#### Validações de Domínios

> **Java:**  DomainValidator.isValid (Apache Commons Validator)
>
> **.Net:**  Uri.CheckHostName (SDK)
>
> **JavaScript:** is-valid-domain
>
> **Python:** validators.domain
>
> **Ruby:** Segundo a OWASP não foi encontrado biblioteca válida.
 
> **Observação**
>
> Não aceite URLs completas nas requisições porque as URLs são difíceis de validar. Se realmente for necessário o envio de endereço de rede, aceite apenas endereços de IP ou nome de domínios válidos.

### Camada de Rede

O objetivo da segurança na Camada de Rede se dá para evitar *VulnerableApplication*, onde as chamdas para outras aplicação não permitas são realizados.


![Esquema do uso de firewall para limitar acessos das aplicações.](image.png)


## Cenários de aplicações em Nuvem

[IMDSv2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/) é um mecanismo adicional de defesa profunda para AWS que mitiga algumas das instâncias de SSRF.

Para aproveitar essa proteção, migre para o IMDSv2 e desative o IMDSv1 antigo. Confira a [documentação da AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) para obter mais detalhes.

<br/>
<br/>
<br/>
<br/>

### Exemplo de um script em Python para monitoramento de IP e Domain.

```Python
# Dependencies: pip install ipaddress dnspython
import ipaddress
import dns.resolver

# Configure the allowlist to check
DOMAINS_ALLOWLIST = ["owasp.org", "labslinux"]

# Configure the DNS resolver to use for all DNS queries
DNS_RESOLVER = dns.resolver.Resolver()
DNS_RESOLVER.nameservers = ["1.1.1.1"]

def verify_dns_records(domain, records, type):
    """
    Verify if one of the DNS records resolve to a non public IP address.
    Return a boolean indicating if any error has been detected.
    """
    error_detected = False
    if records is not None:
        for record in records:
            value = record.to_text().strip()
            try:
                ip = ipaddress.ip_address(value)
                # See https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global
                if not ip.is_global:
                    print("[!] DNS record type '%s' for domain name '%s' resolve to
                    a non public IP address '%s'!" % (type, domain, value))
                    error_detected = True
            except ValueError:
                error_detected = True
                print("[!] '%s' is not valid IP address!" % value)
    return error_detected

def check():
    """
    Perform the check of the allowlist of domains.
    Return a boolean indicating if any error has been detected.
    """
    error_detected = False
    for domain in DOMAINS_ALLOWLIST:
        # Get the IPs of the current domain
        # See https://en.wikipedia.org/wiki/List_of_DNS_record_types
        try:
            # A = IPv4 address record
            ip_v4_records = DNS_RESOLVER.query(domain, "A")
        except Exception as e:
            ip_v4_records = None
            print("[i] Cannot get A record for domain '%s': %s\n" % (domain,e))
        try:
            # AAAA = IPv6 address record
            ip_v6_records = DNS_RESOLVER.query(domain, "AAAA")
        except Exception as e:
            ip_v6_records = None
            print("[i] Cannot get AAAA record for domain '%s': %s\n" % (domain,e))
        # Verify the IPs obtained
        if verify_dns_records(domain, ip_v4_records, "A")
        or verify_dns_records(domain, ip_v6_records, "AAAA"):
            error_detected = True
    return error_detected

if __name__== "__main__":
    if check():
        exit(1)
    else:
        exit(0)
```




