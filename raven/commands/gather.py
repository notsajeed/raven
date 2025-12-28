# raven/commands/gather.py
import click
from raven.git import run_git

@click.command()
def gather():
    """Gather all changes."""
    run_git(["add", "."])
