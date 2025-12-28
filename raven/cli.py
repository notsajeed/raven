import click
from raven.commands.watch import watch
from raven.commands.gather import gather
from raven.commands.mark import mark
from raven.commands.fly import fly

@click.group()
def cli():
    """Raven — a semantic wrapper around Git."""
    pass

cli.add_command(watch)
cli.add_command(gather)
cli.add_command(mark)
cli.add_command(fly)

if __name__ == "__main__":
    cli()
