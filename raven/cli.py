import click
from raven.commands.watch import watch
from raven.commands.gather import gather
from raven.commands.mark import mark

@click.group()
def cli():
    """Raven — a semantic wrapper around Git."""
    pass

cli.add_command(watch)
cli.add_command(gather)
cli.add_command(mark)

if __name__ == "__main__":
    cli()
