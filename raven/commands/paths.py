import click
from raven.git import run_git

@click.command()
def paths():
    """View all branches."""
    run_git(["branch"])
