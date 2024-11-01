import argparse

from . import install, solve


def main():
    """
    Main entry point for Bench.
    """
    description = """
    Bench: PyVRP's benchmarking tool.
    """
    parser = argparse.ArgumentParser(prog="bench", description=description)

    subparsers = parser.add_subparsers(title="subcommands", dest="command")
    install.setup_parser(subparsers)
    solve.setup_parser(subparsers)

    args = parser.parse_args()

    if args.command == "install":
        install.main(**vars(args))
    elif args.command == "solve":
        solve.main(**vars(args))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
