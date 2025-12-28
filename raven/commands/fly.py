# raven/commands/fly.py
import click
from raven.git import run_git

@click.command()
def fly():
    """Send changes to the horizon."""
    run_git(["push"])
