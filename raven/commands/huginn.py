import click
from raven.git import run_git

@click.command()
@click.option("--staged", is_flag=True, help="Show staged diff")
def huginn(staged):
    """Think before acting (diff)."""
    if staged:
        run_git(["diff", "--staged"])
    else:
        run_git(["diff"])
