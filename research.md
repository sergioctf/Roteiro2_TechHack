# Respostas às Perguntas de Pesquisa

# Reconhecimento em Pentest: Ferramentas, Scans e Evasão de IPS

## 1. Ferramentas de Reconhecimento

1. **Shodan**  
   - **O que faz:** Motor de busca de dispositivos conectados à Internet (câmeras IP, SCADA/IoT, roteadores, etc.).  
   - **Exemplo real:** Encontrou estações de tratamento de água desprotegidas, permitindo a pesquisa de serviços vulneráveis em PLCs industriais.  
   - **Fonte:** [Shodan](https://www.shodan.io/)

2. **theHarvester**  
   - **O que faz:** Coleta OSINT de múltiplas fontes (Google, Bing, LinkedIn, certificados SSL) para **e‑mails**, **subdomínios**, nomes de funcionários e IPs associados a um domínio.  
   - **Exemplo real:** `theHarvester -d exemplo.com -b google` extrai e‑mails de funcionários e subdomínios como `vpn.exemplo.com`, auxiliando em campanhas de phishing e mapeamento de VPNs.  
   - **Fonte:** [theHarvester (GitHub)](https://github.com/laramies/theHarvester)

3. **Maltego**  
   - **O que faz:** Plataforma gráfica de OSINT que constrói **grafos relacionais** entre pessoas, domínios, endereços IP, perfis de redes sociais e vazamentos de dados.  
   - **Exemplo real:** Conectou um pseudônimo em fóruns hackers a um perfil de LinkedIn, revelando identidades ocultas.  
   - **Fonte:** [Maltego (Paterva)](https://www.paterva.com/)

4. **OWASP Amass**  
   - **O que faz:** Enumeração extensiva de **subdomínios** e infraestrutura de rede, via reconhecimento passivo e ativo, com armazenamento em banco de dados para correlações futuras.  
   - **Exemplo real:** Descobriu subdomínios esquecidos como `dev.empresa.com` que apontavam para servidores de teste vulneráveis.  
   - **Fonte:** [OWASP Amass (GitHub)](https://github.com/OWASP/Amass)

5. **FOCA**  
   - **O que faz:** Faz *Google/Bing dorks* para baixar documentos (PDF, DOCX, PPTX) de um domínio e extrair **metadados** (nomes de usuários, caminhos de rede, versões de software).  
   - **Exemplo real:** Metadados revelaram nomes de hosts internos e padrões de login da rede corporativa, auxiliando na adivinhação de credenciais.  
   - **Fonte:** [FOCA (GitHub)](https://github.com/ElevenPaths/FOCA)

---

## 2. Scanner de Portas: SYN Scan vs TCP Connect Scan

### TCP SYN Scan (Half‑open)  
- **Funcionamento:** Envia pacote **SYN** → aguarda **SYN/ACK** (porta aberta) ou **RST** (porta fechada) → responde com **RST** para abortar antes do ACK final.  
- **Vantagens:** Rápido, gera menos tráfego e menos conexões completas (mais furtivo).  
- **Requisitos:** Privilégios de root (raw sockets).  
- **Quando usar:** Mapeamento rápido e discreto de portas em servidores externos.  
- **Fonte:** [Nmap SYN Scan](https://nmap.org/book/man-port-scanning-techniques.html#port-scanning-syn-scan)

### TCP Connect Scan (Full Connect)  
- **Funcionamento:** Usa a API `connect()` do SO para completar o **3‑way handshake** (SYN → SYN/ACK → ACK) e depois encerra (FIN/RST).  
- **Vantagens:** Não requer privilégios especiais; funciona em qualquer SO.  
- **Desvantagens:** Mais lento, mais detectável (conexões completas registradas em logs).  
- **Quando usar:** Ambientes restritos (sem acesso a raw sockets) ou quando a conclusão da sessão for necessária.  
- **Fonte:** [Nmap Connect Scan](https://nmap.org/book/man-port-scanning-techniques.html#port-scanning-connect-scan)

---

## 3. Técnicas de Evasão de IPS Durante Reconhecimento

1. **Fragmentação de Pacotes**  
   - **O que faz:** Divide pacotes IP em fragmentos pequenos para burlar assinaturas de IPS.  
   - **Impacto:** Pode driblar IPS que não remontam fragmentos, mas reduz a velocidade e pode falhar se fragmentos forem bloqueados.  
   - **Como usar:** `nmap -f alvo`  
   - **Fonte:** [Nmap IP Fragmentation](https://nmap.org/book/man-port-scanning-techniques.html#fragmentation)

2. **Varredura “Low and Slow”**  
   - **O que faz:** Envia sondas muito espaçadas (`-T0`, `-T1`) ou usa múltiplos IPs de origem para ficar abaixo de limiares de detecção.  
   - **Impacto:** Alta furtividade; varredura pode levar horas ou dias.  
   - **Fonte:** [Nmap Timing Templates](https://nmap.org/book/performance-timing.html)

3. **Uso de Proxies / TOR**  
   - **O que faz:** Encaminha tráfego via servidores proxy, VPN ou rede Tor para mascarar o IP real do pentester.  
   - **Impacto:** Confunde logs do IPS; mas pode limitar técnicas de scan raw e introduzir latência.  
   - **Ferramenta exemplo:** [ProxyChains‑NG](https://github.com/rofl0r/proxychains-ng)

4. **Spoofing de IP e Decoys**  
   - **O que faz:** Forja IPs de origem ou mistura sondas legítimas com decoys (`-D IP1,IP2,...`) para ocultar o scanner real.  
   - **Impacto:** Complica a atribuição de bloqueios; porém aumenta o volume de tráfego e pode atrasar o scan.  
   - **Fonte:** [Nmap Decoy Scan](https://nmap.org/book/man-port-scanning-techniques.html#decoy-scan)

5. **Idle Scan**  
   - **O que faz:** Usa um “zumbi” com IP spoofed para sondar o alvo, sem revelar o IP do pentester.  
   - **Impacto:** Máxima furtividade de origem; requer um host zumbi com IP pré‑conhecido.  
   - **Fonte:** [Nmap Idle Scan](https://nmap.org/book/man-port-scanning-techniques.html#idlescan)

6. **Evasão Genérica de IDS/IPS**  
   - **O que faz:** Combina obfuscação de payload, alteração de TTL, randomização de portas de origem, e horários fora de pico para confundir sistemas de detecção.  
   - **Impacto:** Dificulta a correlação de eventos; nenhum método é infalível contra IPS modernos.  
   - **Fonte:** [Intrusion Detection Evasion Techniques and Case Studies (SANS)](https://www.sans.org/reading-room/whitepapers/detection/intrusion-detection-evasion-techniques-case-studies-37527)

---

## Referências que usei para responder e aprender sobre o assunto:

- Shodan – https://www.shodan.io/  
- theHarvester – https://github.com/laramies/theHarvester  
- Maltego – https://www.paterva.com/  
- OWASP Amass – https://github.com/OWASP/Amass  
- FOCA – https://github.com/ElevenPaths/FOCA  
- Nmap SYN Scan – https://nmap.org/book/man-port-scanning-techniques.html#port-scanning-syn-scan  
- Nmap Connect Scan – https://nmap.org/book/man-port-scanning-techniques.html#port-scanning-connect-scan  
- Nmap IP Fragmentation – https://nmap.org/book/man-port-scanning-techniques.html#fragmentation  
- Nmap Timing Templates – https://nmap.org/book/performance-timing.html  
- Nmap Decoy Scan – https://nmap.org/book/man-port-scanning-techniques.html#decoy-scan  
- Nmap Idle Scan – https://nmap.org/book/man-port-scanning-techniques.html#idlescan  
- ProxyChains‑NG – https://github.com/rofl0r/proxychains-ng  
- SANS “Intrusion Detection Evasion Techniques and Case Studies” – https://www.sans.org/reading-room/whitepapers/detection/intrusion-detection-evasion-techniques-case-studies-37527  

**Nota:** O uso de AI nessa parte foi somente para ajudar a estruturar o texto e não para gerar conteúdo. Todo o conteúdo foi escrito por mim, com base em minhas pesquisas e aprendizado.