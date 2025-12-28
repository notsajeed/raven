import click
from raven.git import run_git

@click.command()
@click.argument("branch")
def spawn(branch):
    """Create a new branch."""
    run_git(["checkout", "-b", branch])
