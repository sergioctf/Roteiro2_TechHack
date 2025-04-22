# reconapp/whois_lookup.py

import whois

def whois_lookup(domain: str) -> str:
    """
    Consulta WHOIS e formata as principais informações.
    """
    try:
        w = whois.whois(domain)
    except Exception as e:
        return f"Error: {e}"

    fields = [
        ("Domain Name", w.domain_name),
        ("Registrar", w.registrar),
        ("Creation Date", w.creation_date),
        ("Expiration Date", w.expiration_date),
        ("Name Servers", w.name_servers),
        ("Emails", w.emails),
    ]
    lines = []
    for label, val in fields:
        if val:
            lines.append(f"{label}: {val}")
    return "\n".join(lines) or "No WHOIS data"
