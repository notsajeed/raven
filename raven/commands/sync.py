import click
from raven.git import run_git

@click.command()
def sync():
    """Sync with remote."""
    run_git(["pull"])
