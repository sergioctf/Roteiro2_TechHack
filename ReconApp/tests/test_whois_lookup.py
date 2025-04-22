import pytest
from reconapp.whois_lookup import whois_lookup

class DummyWhois:
    def __init__(self):
        self.domain_name = "EXAMPLE.COM"
        self.registrar = "IANA"
        self.creation_date = "1995-08-14"
        self.expiration_date = "2025-08-13"
        self.name_servers = ["A.IANA.NET"]
        self.emails = ["hostmaster@example.com"]

def test_whois_success(monkeypatch):
    monkeypatch.setattr("whois.whois", lambda d: DummyWhois())
    out = whois_lookup("example.com")
    assert "Domain Name: EXAMPLE.COM" in out
    assert "Registrar: IANA" in out

def test_whois_error(monkeypatch):
    monkeypatch.setattr("whois.whois", lambda d: (_ for _ in ()).throw(Exception("fail")))
    assert "Error: fail" in whois_lookup("example.com")
