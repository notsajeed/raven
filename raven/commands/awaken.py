import click
from raven.git import run_git

@click.command()
def awaken():
    """Awaken a new repository."""
    run_git(["init"])
