# reconapp/cli.py

import click
from tabulate import tabulate

from .portscan import parse_ports, scan_ports
from .subdomain_enum import enum_subdomains
from .whois_lookup import whois_lookup
from .theharvester import run_harvester
from .waf_detection import detect_waf

@click.group()
def cli():
    """ReconApp – Ferramenta modular de reconhecimento."""
    pass

@cli.command()
@click.option("--host", "-h", default="127.0.0.1", help="Host alvo")
@click.option("--ports", "-p", default="1-1000", help="Faixa de portas (ex: 1-1000)")
@click.option("--timeout", "-t", default=1.0, type=float, help="Timeout por porta")
def portscan(host, ports, timeout):
    """Executa PortScan."""
    ports_list = parse_ports(ports)
    results = scan_ports(host, ports_list, timeout)
    click.echo(tabulate(results, headers=["Porta", "Status"], tablefmt="github"))

@cli.command()
@click.option("--domain", "-d", required=True, help="Domínio para enumeração")
@click.option("--output", "-o", type=click.Path(), help="Gravar em arquivo")
def subdomain(domain, output):
    """Enumeração de subdomínios."""
    subs = enum_subdomains(domain)
    for s in subs:
        click.echo(s)
    if output:
        open(output, "w").write("\n".join(subs))

@cli.command()
@click.option("--domain", "-d", required=True, help="Domínio para WHOIS")
def whois(domain):
    """Consulta WHOIS."""
    click.echo(whois_lookup(domain))

@cli.command()
@click.option("--domain", "-d", required=True, help="Domínio para OSINT")
@click.option("--source", "-b", default="bing", help="Fonte (bing,yahoo,github…)") 
def theharvester(domain, source):
    """Coleta OSINT com theHarvester."""
    for line in run_harvester(domain, source):
        click.echo(line)

@cli.command()
@click.option("--url", "-u", required=True, help="URL para detecção de WAF")
def waf(url):
    """Detecção de WAF."""
    click.echo(detect_waf(url))

@cli.command()
def version():
    """Exibe versão."""
    click.echo("ReconApp v0.1.0")

if __name__ == "__main__":
    cli()
