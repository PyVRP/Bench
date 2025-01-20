import argparse
import subprocess
import sys
from importlib.util import find_spec

from . import solve


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


def install(repository: str, revision: str):
    """
    Installs PyVRP from GitHub.

    Parameters
    ----------
    repository
        The GitHub repository to install.
    revision
        The revision to install.
    """
    if is_installed():
        uninstall()

    url = f"git+https://github.com/{repository}@{revision}"
    cmd = [sys.executable, "-m", "pip", "install", url]
    subprocess.check_call(cmd)


def main():
    description = """
    Bench: PyVRP's benchmarking tool.
    """
    parser = argparse.ArgumentParser(prog="bench", description=description)

    subparsers = parser.add_subparsers(title="subcommands", dest="command")
    solve.setup_parser(subparsers)

    msg = "Install PyVRP from Github."
    subparser = subparsers.add_parser("install", description=msg, help=msg)

    msg = "Github repository to install PyVRP."
    subparser.add_argument(
        "--repository", type=str, default="PyVRP/PyVRP", help=msg
    )

    msg = "Revision to install."
    subparser.add_argument("--revision", type=str, default="main", help=msg)

    msg = "Uninstall PyVRP."
    subparsers.add_parser("uninstall", description=msg, help=msg)

    args = parser.parse_args()

    if args.command == "solve":
        solve.main(**vars(args))
    elif args.command == "install":
        install(args.repository, args.revision)
    elif args.command == "uninstall":
        uninstall()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
