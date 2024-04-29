import argparse
from .cli_commands import subcommands

def main():
    parser = argparse.ArgumentParser(description='Web Harvester CLI')
    parser.set_defaults(func=lambda _: parser.print_help())
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
    for name, subcommand in subcommands.items():
        subparsers.add_parser(name, parents=[subcommand])
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()