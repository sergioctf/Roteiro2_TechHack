# reconapp/waf_detection.py

import subprocess
import re

def detect_waf(url: str) -> str:
    """
    Executa o wafw00f via CLI e parseia a saída de texto:
      - Se encontra linhas “[+] The site … is behind X WAF.”, retorna “WAF: X WAF”.
      - Se encontra “No WAF detected”, retorna “No WAF detected”.
      - Caso contrário, retorna “Unable to detect WAF”.
    """
    cmd = ["wafw00f", url]
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        return "Error: wafw00f not installed"
    except subprocess.CalledProcessError as e:
        out = e.output or ""

    wafs = set()
    for line in out.splitlines():
        m = re.search(r"\[\+\]\s+The site .* is behind (.+? WAF)\b", line)
        if m:
            wafs.add(m.group(1))

    if wafs:
        return "\n".join(f"WAF: {w}" for w in sorted(wafs))
    if any("No WAF detected" in line for line in out.splitlines()):
        return "No WAF detected"
    return "Unable to detect WAF"
