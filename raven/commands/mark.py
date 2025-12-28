# raven/commands/mark.py
import click
from raven.git import run_git

@click.command()
@click.argument("message")
def mark(message):
    """Record a memory (commit)."""
    run_git(["commit", "-m", message])
