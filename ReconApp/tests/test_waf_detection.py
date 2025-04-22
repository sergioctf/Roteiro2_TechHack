import pytest
from reconapp.waf_detection import detect_waf

def test_waf_not_installed(monkeypatch):
    import subprocess
    monkeypatch.setattr(subprocess, "check_output", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError))
    assert "Error: wafw00f not installed" == detect_waf("https://example.com")

def test_waf_no_detect(monkeypatch):
    import subprocess
    monkeypatch.setattr(subprocess, "check_output", lambda *a, **k: "[*] No WAF detected\n")
    assert detect_waf("https://example.com") == "No WAF detected"
