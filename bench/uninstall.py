import subprocess
import sys
from importlib.util import find_spec


def is_installed() -> bool:
    """
    Checks if PyVRP is already installed.
    """
    return find_spec("pyvrp") is not None


def uninstall():
    """
    Uninstalls any previously installed version of PyVRP.
    """
    cmd = [sys.executable, "-m", "pip", "uninstall", "-y", "pyvrp"]
    subprocess.check_call(cmd)


def setup_parser(subparsers):
    msg = "Uninstall the PyVRP solver."
    return subparsers.add_parser("uninstall", description=msg, help=msg)


def main(**kwargs):
    if is_installed():
        uninstall()
