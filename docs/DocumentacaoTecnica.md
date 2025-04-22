# Documentação Técnica – ReconApp

---

## Índice

1. [Visão Geral](#visão-geral)  
2. [Estrutura do Projeto](#estrutura-do-projeto)  
3. [Módulos Principais](#módulos-principais)  
   3.1. [cli.py](#cli-py)  
   3.2. [portscan.py](#portscan-py)  
   3.3. [subdomain_enum.py](#subdomain_enum-py)  
   3.4. [whois_lookup.py](#whois_lookup-py)  
   3.5. [theharvester.py](#theharvester-py)  
   3.6. [waf_detection.py](#waf_detection-py)  
4. [Fluxo de Execução](#fluxo-de-execução)  
5. [Decisões de Design](#decisões-de-design)  
6. [Testes](#testes)  

---

## Visão Geral

O **ReconApp** é uma CLI em Python que centraliza as tarefas de reconhecimento em testes de invasão, integrando módulos de varredura de portas, enumeração de subdomínios, consultas WHOIS, coleta OSINT e detecção de WAF.

---

## Estrutura do Projeto

```text
ReconApp/
├── .venv/                 # Ambiente virtual Python
├── reconapp/              # Package com código-fonte
│   ├── __init__.py
│   ├── cli.py
│   ├── portscan.py
│   ├── subdomain_enum.py
│   ├── whois_lookup.py
│   ├── theharvester.py
│   └── waf_detection.py
├── tests/                 # Testes unitários (pytest)
├── setup.py               # Configuração do package
└── requirements.txt       # Dependências Python
docs/                  # Documentação (manual, técnica)
README.md              # Apresentação do projeto
research.md            # Respostas às Perguntas de Pesquisa
```

---

## Módulos Principais

### cli.py

- Utiliza **Click** para definir a interface de linha de comando modular.  
- Orquestra chamadas para cada subcomando e formata saída (ex.: **Tabulate**).

### portscan.py

- `parse_ports()`: converte string de faixas e portas em lista de inteiros.  
- `scan_ports()`: varre portas TCP usando sockets, retornando status “open” ou “closed”.

### subdomain_enum.py

- Executa **sublist3r** via subprocesso, salvando saída em arquivo temporário e retornando lista de subdomínios.

### whois_lookup.py

- Usa biblioteca **python-whois** para obter e formatar registrar, datas, servidores e e‑mails.

### theharvester.py

- Invoca CLI **theHarvester** via subprocess, retornando linhas de saída bruta.

### waf_detection.py

- Invoca CLI **wafw00f** via subprocess e parseia saída textual para identificar WAFs ou indicar ausência.

---

## Fluxo de Execução

1. Usuário chama `reconapp [comando]`.  
2. **cli.py** parseia opções e invoca módulo correspondente.  
3. O módulo executa lógica interna (socket, subprocess, biblioteca) e retorna dados.  
4. **cli.py** exibe resultado de forma formatada ao usuário.

---

## Decisões de Design

- **Modularidade**: cada funcionalidade isolada em arquivo próprio, facilitando manutenção e extensões.  
- **Click**: simplifica criação de CLI com menus, flags e ajuda automática.  
- **Tabulate**: gera tabelas legíveis na saída do terminal para PortScan.  
- **Subprocessos**: evita reimplementação de ferramentas maduras (theHarvester, wafw00f, sublist3r).  
- **Testes automatizados**: pytest com monkeypatch para simular diferentes cenários e garantir qualidade.

---

## Testes

- Localizados em `tests/` e rodados via `pytest -q`.  
- Cobrem:  
  - Parsing e varredura de portas  
  - Erros de dependência e falhas de subprocessos  
  - Formatação de saída WHOIS, subdomínio, OSINT e WAF  
- Todas as suítes retornam **OK**, garantindo 100% de conformidade.  
