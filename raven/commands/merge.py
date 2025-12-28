import click
from raven.git import run_git

@click.command()
@click.argument("branch")
def merge(branch):
    """Merge a branch."""
    run_git(["merge", branch])
