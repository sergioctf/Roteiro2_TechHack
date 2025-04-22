import pytest
from reconapp.portscan import parse_ports, scan_ports

def test_parse_ports_single_and_ranges():
    assert parse_ports("1-3,5,7-8") == [1,2,3,5,7,8]
    assert parse_ports("22") == [22]

def test_scan_ports_closed(monkeypatch):
    # Simula host fechado em todas as portas
    class FakeSocket:
        def __init__(self, *args, **kwargs): pass
        def settimeout(self, t): pass
        def connect(self, addr): raise ConnectionRefusedError
        def close(self): pass

    monkeypatch.setattr("reconapp.portscan.socket.socket", lambda *a,**k: FakeSocket())
    results = scan_ports("1.2.3.4", [80, 443], timeout=0.1)
    assert results == [(80, "closed"), (443, "closed")]

def test_scan_ports_open(monkeypatch):
    # Simula host aberto em todas as portas
    class FakeSocket:
        def __init__(self, *args, **kwargs): pass
        def settimeout(self, t): pass
        def connect(self, addr): pass
        def close(self): pass

    monkeypatch.setattr("reconapp.portscan.socket.socket", lambda *a,**k: FakeSocket())
    results = scan_ports("1.2.3.4", [22], timeout=0.1)
    assert results == [(22, "open")]
