import subprocess
import sys

from .uninstall import is_installed, uninstall


def install(revision: str = "main"):
    """
    Installs a specific revision of PyVRP from GitHub.
    """
    url = f"git+https://github.com/pyvrp/pyvrp@{revision}#egg=pyvrp"
    cmd = [sys.executable, "-m", "pip", "install", url]
    subprocess.check_call(cmd)


def setup_parser(subparsers):
    msg = "Install the PyVRP solver."
    parser = subparsers.add_parser("install", description=msg, help=msg)

    msg = "Revision to install from PyVRP's GitHub repository."
    parser.add_argument("--revision", default="main", type=str, help=msg)


def main(revision: str, **kwargs):
    if is_installed():
        uninstall()

    install(revision)
