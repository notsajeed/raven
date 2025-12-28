import click
from raven.git import run_git

@click.command()
def mark():
    """Observe repository state."""
    run_git(["status"])

