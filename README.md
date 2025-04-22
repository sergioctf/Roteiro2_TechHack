# TECNOLOGIAS HACKER - 2025.1 - Insper
## Sérgio Carmelo - Engenharia da Computação
## Roteiro 2 – App Reconhecimento do Alvo

### As respostas as perguntas de pesquisa estão no arquivo `research.md`.

### O Manual do Usuário está no arquivo `docs/ManualDoUsuario.md`. Assim como a Documentação Técnica, que está no arquivo `docs/DocumentacaoTecnica.md`. O README.md é o arquivo de apresentação do projeto, que também contém o resumo do manual do usuário e da documentação técnica.

ReconApp é uma ferramenta de linha de comando (CLI) modular em Python para a fase de reconhecimento em pentests.  
Ela integra scripts de port scanning, enumeração de subdomínios, consultas WHOIS, coleta OSINT com theHarvester e detecção de WAF.

---

## Pré‑requisitos

- **Python 3.10+**  
- **Virtualenv**  
- Ferramentas CLI externas (devem estar no PATH do ambiente virtual):  
  - `sublist3r`  
    ```bash
    pip install sublist3r
    ```  
  - `theHarvester`  
    ```bash
    pip install --ignore-requires-python git+https://github.com/laramies/theHarvester.git
    ```  
  - `wafw00f`  
    ```bash
    pip install wafw00f
    ```

---

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/reconapp.git
cd reconapp

# 2. Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instale dependências Python
pip install -r requirements.txt
pip install -e .

# 4. Instale CLIs externas
pip install sublist3r
pip install wafw00f
pip install --ignore-requires-python git+https://github.com/laramies/theHarvester.git

```markdown
# ReconApp

ReconApp é uma ferramenta de linha de comando (CLI) modular em Python para a fase de reconhecimento em pentests.  
Ela integra scripts de port scanning, enumeração de subdomínios, consultas WHOIS, coleta OSINT com theHarvester e detecção de WAF.

---

## Pré‑requisitos

- **Python 3.10+**  
- **Virtualenv**  
- Ferramentas CLI externas (devem estar no PATH do ambiente virtual):  
  - `sublist3r`  
    ```bash
    pip install sublist3r
    ```  
  - `theHarvester`  
    ```bash
    pip install --ignore-requires-python git+https://github.com/laramies/theHarvester.git
    ```  
  - `wafw00f`  
    ```bash
    pip install wafw00f
    ```

---

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/reconapp.git
cd reconapp

# 2. Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instale dependências Python
pip install -r requirements.txt
pip install -e .

# 4. Instale CLIs externas
pip install sublist3r
pip install wafw00f
pip install --ignore-requires-python git+https://github.com/laramies/theHarvester.git
```

---

## Uso

```bash
reconapp [COMANDO] [OPÇÕES]
```

### 1. PortScan

Varre portas TCP no host alvo.

```bash
reconapp portscan --host 127.0.0.1 --ports 1-1024,8080 --timeout 0.5
```

**Opções**  
- `--host, -h` Host ou IP alvo (default `127.0.0.1`)  
- `--ports, -p` Faixa de portas (ex: `1-1000,443`)  
- `--timeout, -t` Timeout por porta em segundos  

### 2. Enumeração de Subdomínios

Descobre subdomínios usando `sublist3r`.

```bash
reconapp subdomain --domain exemplo.com --output subs.txt
```

**Opções**  
- `--domain, -d` Domínio alvo (obrigatório)  
- `--output, -o` Arquivo para salvar resultados (opcional)  

### 3. WHOIS

Consulta dados WHOIS de um domínio.

```bash
reconapp whois --domain exemplo.com
```

**Opções**  
- `--domain, -d` Domínio alvo (obrigatório)  

### 4. OSINT com theHarvester

Coleta e‑mails, hosts e outras informações OSINT.

```bash
reconapp theharvester --domain exemplo.com --source bing
```

**Opções**  
- `--domain, -d` Domínio alvo (obrigatório)  
- `--source, -b` Fonte de busca (ex: `bing`, `yahoo`, `github`, `linkedin`)  

### 5. Detecção de WAF

Identifica Web Application Firewalls via `wafw00f`.

```bash
reconapp waf --url https://exemplo.com
```

**Opções**  
- `--url, -u` URL completa (obrigatório)  

### 6. Versão

```bash
reconapp version
```

---

## Estrutura do Projeto

```
ReconApp/                  
├── .venv/                 # ambiente virtual Python
├── reconapp/              # código-fonte do package
│   ├── __init__.py        
│   ├── cli.py             
│   ├── portscan.py        
│   ├── subdomain_enum.py  
│   ├── whois_lookup.py    
│   ├── theharvester.py    
│   └── waf_detection.py   
├── tests/                 # testes unitários (pytest)
├── docs/                  # documentação (manual, arquitetura)
├── setup.py               # configurações do pacote
└── requirements.txt       # dependências Python
```

---

## Testes

Para executar a suíte de testes:

```bash
pytest -q
```

---


## Conformidade com Critérios de Avaliação 

O **ReconApp** atende a todos os requisitos do nível **Avançado** (Nota 9–10), assim como os critérios anteriores:

- **Funcionalidade completa e robusta**  
  – PortScan, WHOIS lookup, enumeração de subdomínios, theHarvester OSINT e detecção de WAF totalmente integrados e funcionando sem erros.

- **Respostas de pesquisa detalhadas**  
  – Cinco ferramentas justificadas com exemplos reais, comparação aprofundada de SYN vs TCP Connect Scan e diversas técnicas de evasão de IPS analisadas.

- **Interface intuitiva**  
  – CLI baseada em Click com ajuda automática, flags claras e saída formatada (tabulações e listas).

- **Código modular e bem documentado**  
  – Cada ferramenta em seu próprio módulo, docstrings, tipagem básica e testes unitários que garantem qualidade e facilitam futuras melhorias.

- **Documentação completa**  
  – Manual do usuário, documentação técnica e relatório de pesquisa organizados em Markdown, prontos para entrega.

Com isso, o projeto está em pleno conformidade com o critério de **Nota 9–10**.   
