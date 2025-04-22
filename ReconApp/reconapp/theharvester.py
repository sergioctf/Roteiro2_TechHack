# reconapp/theharvester.py

import subprocess


def run_harvester(domain: str, source: str) -> list[str]:
    """
    Chama o CLI theHarvester (pip install git+https://github.com/laramies/theHarvester.git).
    """
    cmd = ["theHarvester", "-d", domain, "-b", source]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
        return out.splitlines()
    except FileNotFoundError:
        return ["Error: theHarvester not installed"]
    except Exception as e:
        return [f"Error running theHarvester: {e}"]
