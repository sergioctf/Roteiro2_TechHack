# reconapp/subdomain_enum.py

import subprocess
import tempfile
import os

def enum_subdomains(domain: str) -> list[str]:
    """
    Chama o CLI sublist3r para enumeração de subdomínios.
    Requer: pip install sublist3r
    """
    # arquivo temporário para saída
    with tempfile.NamedTemporaryFile(delete=False, mode="w+") as tmp:
        tmp_path = tmp.name

    cmd = ["sublist3r", "-d", domain, "-o", tmp_path]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with open(tmp_path) as f:
            subs = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        subs = []
    finally:
        os.remove(tmp_path)

    return subs
