import click
from raven.git import run_git

@click.command()
@click.option("--oneline", is_flag=True, help="Compact history")
def muninn(oneline):
    """Recall memory (history)."""
    if oneline:
        run_git(["log", "--oneline"])
    else:
        run_git(["log"])
