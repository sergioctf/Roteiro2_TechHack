# Manual do Usuário – ReconApp

---

## Índice

1. [Introdução](#introdução)  
2. [Requisitos](#requisitos)  
3. [Instalação](#instalação)  
4. [Uso](#uso)  
   4.1. [PortScan](#portscan)  
   4.2. [Enumeração de Subdomínios](#enumeração-de-subdomínios)  
   4.3. [WHOIS](#whois)  
   4.4. [OSINT com theHarvester](#osint-com-theharvester)  
   4.5. [Detecção de WAF](#detecção-de-waf)  
   4.6. [Versão](#versão)  
5. [Exemplos de Fluxo](#exemplos-de-fluxo)  
6. [Suporte](#suporte)

---

## Introdução

O **ReconApp** é uma ferramenta de linha de comando (CLI) modular em Python voltada para a fase de reconhecimento em testes de invasão (pentests).  
Ela unifica as principais funcionalidades de:

- Varredura de portas (PortScan)  
- Enumeração de subdomínios (DNS lookup)  
- Consultas WHOIS  
- Coleta OSINT (theHarvester)  
- Detecção de Web Application Firewalls (wafw00f)  

---

## Requisitos

- **Sistema Operacional**: Linux (testado em Ubuntu 22.04)  
- **Python**: versão 3.10 ou superior  
- **Ambiente Virtual**: `venv` ou similar  
- **Ferramentas Externas no PATH**:  
  - `sublist3r`  
  - `theHarvester` (>=4.7.1)  
  - `wafw00f`  

---

## Instalação

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/SEU_USUARIO/reconapp.git
   cd reconapp
   ```

2. **Crie e ative o ambiente virtual**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale dependências Python**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Instale CLIs externas**  
   ```bash
   pip install sublist3r
   pip install wafw00f
   pip install --ignore-requires-python git+https://github.com/laramies/theHarvester.git
   ```

---

## Uso

```bash
reconapp [COMANDO] [OPÇÕES]
```

### 4.1. PortScan

Varre portas TCP em um host de destino.

```bash
reconapp portscan --host 127.0.0.1 --ports 1-1024,8080 --timeout 0.5
```

- `--host, -h` Host ou IP alvo (padrão: `127.0.0.1`)  
- `--ports, -p` Faixa de portas (ex.: `1-1000,443`)  
- `--timeout, -t` Timeout por porta em segundos  

### 4.2. Enumeração de Subdomínios

Descobre subdomínios de um domínio usando `sublist3r`.

```bash
reconapp subdomain --domain exemplo.com --output subs.txt
```

- `--domain, -d` Domínio alvo (obrigatório)  
- `--output, -o` Arquivo de saída (opcional)  

### 4.3. WHOIS

Exibe informações WHOIS de um domínio.

```bash
reconapp whois --domain exemplo.com
```

- `--domain, -d` Domínio alvo (obrigatório)  

### 4.4. OSINT com theHarvester

Coleta e‑mails, hosts e outras informações OSINT.

```bash
reconapp theharvester --domain exemplo.com --source bing
```

- `--domain, -d` Domínio alvo (obrigatório)  
- `--source, -b` Fonte de busca (ex.: `bing`, `yahoo`, `github`, `linkedin`)  

### 4.5. Detecção de WAF

Identifica Web Application Firewalls.

```bash
reconapp waf --url https://exemplo.com
```

- `--url, -u` URL completa (obrigatório)  

### 4.6. Versão

```bash
reconapp version
```

---

## Exemplos de Fluxo

```bash
$ reconapp
Bem‑vind@ ao ReconApp!
1) PortScan
2) Subdomain Enumeration
3) WHOIS Lookup
4) theHarvester
5) WAF Detection
6) Sair
Escolha uma opção [1‑6]:
```

---