import subprocess
import sys

from pkg_resources import DistributionNotFound, get_distribution


def is_installed() -> bool:
    """
    Checks if PyVRP is already installed.
    """
    try:
        get_distribution("pyvrp")
        return True
    except DistributionNotFound:
        return False


def uninstall():
    """
    Uninstalls any previously installed version of PyVRP.
    """
    cmd = [sys.executable, "-m", "pip", "uninstall", "-y", "pyvrp"]
    subprocess.check_call(cmd)


def install(commit: str):
    """
    Installs a specific commit of PyVRP from GitHub.
    """
    url = f"git+https://github.com/PyVRP/PyVRP@{commit}#egg=PyVRP"
    cmd = [sys.executable, "-m", "pip", "install", url]
    subprocess.check_call(cmd)


def setup_parser(subparsers):
    msg = "Install a specific commit of PyVRP from GitHub."
    parser = subparsers.add_parser("install", description=msg, help=msg)

    msg = "Commit hash to install from PyVRP's GitHub repository."
    parser.add_argument("commit", type=str, help=msg)

    # TODO install main by default?


def main(commit: str, **kwargs):
    if is_installed():
        uninstall()

    install(commit)
