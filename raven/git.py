# raven/git.py
import subprocess
import sys

def run_git(args):
    result = subprocess.run(
        ["git"] + args,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    if result.returncode != 0:
        sys.exit(result.returncode)
