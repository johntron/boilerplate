import argparse

def setup(args):
    print('Setting up the web harvester...')

parser = argparse.ArgumentParser(add_help=False)
parser.set_defaults(func=setup)