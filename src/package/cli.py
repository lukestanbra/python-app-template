"""This is a module docstring"""

import argparse
from package.hello_world import hello_world

parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument(
    'names',
    metavar='NAME',
    nargs=argparse.ZERO_OR_MORE,
    help="A name of something.")

def main(args=None):
    """Main entry point

    Args:
        args (list, optional): Command line arguments. Defaults to None.
    """
    args = parser.parse_args(args=args)
    hello_world()
    print(args.names)
