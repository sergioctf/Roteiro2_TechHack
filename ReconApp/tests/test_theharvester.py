import pytest
from reconapp.theharvester import run_harvester

def test_harvester_not_installed(monkeypatch):
    import subprocess
    monkeypatch.setattr(subprocess, "check_output", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError))
    assert run_harvester("example.com", "bing") == ["Error: theHarvester not installed"]

def test_harvester_error(monkeypatch):
    import subprocess
    class CalledProcessError(Exception):
        returncode = 2
    monkeypatch.setattr(subprocess, "check_output", lambda *a, **k: (_ for _ in ()).throw(CalledProcessError()))
    res = run_harvester("example.com", "bing")
    assert "Error running theHarvester" in res[0]
