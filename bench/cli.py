import argparse
import subprocess
import sys
from importlib.util import find_spec

from . import solve


def main():
    """
    Main entry point for Bench.
    """
    description = """
    Bench: PyVRP's benchmarking tool.
    """
    parser = argparse.ArgumentParser(prog="bench", description=description)

    subparsers = parser.add_subparsers(title="subcommands", dest="command")
    solve.setup_parser(subparsers)

    msg = "Install PyVRP."
    subparser = subparsers.add_parser("install", description=msg, help=msg)

    msg = "Revision to install from PyVRP's GitHub repository."
    subparser.add_argument("--revision", default="main", type=str, help=msg)

    msg = "Uninstall PyVRP."
    subparsers.add_parser("uninstall", description=msg, help=msg)

    args = parser.parse_args()

    if args.command == "install":
        install(args.revision)
    elif args.command == "uninstall":
        uninstall()
    elif args.command == "solve":
        solve.main(**vars(args))
    else:
        parser.print_help()


def is_installed() -> bool:
    """
    Checks if PyVRP is already installed.
    """
    return find_spec("pyvrp") is not None


def uninstall():
    """
    Uninstalls any previously installed version of PyVRP.
    """
    if not is_installed():
        print("PyVRP is currently not installed.")
        return

    cmd = [sys.executable, "-m", "pip", "uninstall", "-y", "pyvrp"]
    subprocess.check_call(cmd)


def install(revision: str):
    """
    Installs a specific revision of PyVRP from GitHub.
    """
    if is_installed():
        uninstall()

    url = f"git+https://github.com/pyvrp/pyvrp@{revision}#egg=pyvrp"
    cmd = [sys.executable, "-m", "pip", "install", url]
    subprocess.check_call(cmd)


if __name__ == "__main__":
    main()
