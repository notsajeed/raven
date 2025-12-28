import click
from raven.git import run_git

@click.command()
@click.argument("branch")
def perch(branch):
    """Switch branches."""
    run_git(["checkout", branch])
