import pytest
import tempfile
from reconapp import subdomain_enum

def test_enum_subdomains_no_cli(monkeypatch):
    # Simula FileNotFoundError quando sublist3r não está instalado
    monkeypatch.setattr("subprocess.run", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError))
    assert subdomain_enum.enum_subdomains("example.com") == []
