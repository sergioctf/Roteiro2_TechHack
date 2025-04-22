# reconapp/portscan.py

import socket
from typing import List, Tuple

def parse_ports(port_str: str) -> List[int]:
    """
    Converte strings como "1-3,22,80-82" em [1,2,3,22,80,81,82].
    """
    ports = set()
    for part in port_str.split(","):
        if "-" in part:
            start, end = part.split("-", 1)
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)

def scan_ports(host: str, ports: List[int], timeout: float = 1.0) -> List[Tuple[int, str]]:
    """
    Varre cada porta em `ports` no `host`, com timeout (s).
    Retorna lista de tuplas (porta, "open"|"closed").
    """
    results: List[Tuple[int, str]] = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            results.append((port, "open"))
        except (socket.timeout, ConnectionRefusedError, OSError):
            results.append((port, "closed"))
        finally:
            sock.close()
    return results
