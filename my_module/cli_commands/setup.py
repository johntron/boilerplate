import argparse
import pathlib
import shlex
import subprocess
import sys

project_root = pathlib.Path(__file__).parent.parent.parent

def _run(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = result.stdout.decode("utf-8")
    stderr = result.stderr.decode("utf-8")
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}")
        print("Standard Output:")
        print(stdout)
        print("Standard Error:")
        print(stderr, file=sys.stderr)
        exit(1)
    return stdout

def create_venv():
    print("Creating virtual env at .venv")
    command = shlex.split("python3.12 -m venv .venv")
    _run(command)


def install_deps():
    print("Installing dependencies")
    command = shlex.split(
        f"{project_root}/.venv/bin/pip install -r {project_root}/requirements.txt"
    )
    _run(command)

def setup(args):
    print('Setting up the web harvester...')
    create_venv()
    install_deps()

def print_usage():
    print("Done")
    print("Activate the virtual environment by running:")
    print()
    print("source .venv/bin/activate")

parser = argparse.ArgumentParser(add_help=False)
parser.set_defaults(func=setup)