import click
from raven.commands.watch import watch

@click.group()
def cli():
    """Raven — a semantic wrapper around Git."""
    pass

cli.add_command(watch)

if __name__ == "__main__":
    cli()
