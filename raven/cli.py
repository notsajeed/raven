import click

from raven.commands.watch import watch
from raven.commands.gather import gather
from raven.commands.mark import mark
from raven.commands.fly import fly
from raven.commands.sync import sync
from raven.commands.huginn import huginn
from raven.commands.muninn import muninn
from raven.commands.paths import paths
from raven.commands.perch import perch
from raven.commands.spawn import spawn
from raven.commands.merge import merge
from raven.commands.awaken import awaken

@click.group()
def cli():
    """Raven — send ravens instead of Git commands."""
    pass

cli.add_command(watch)
cli.add_command(gather)
cli.add_command(mark)
cli.add_command(fly)
cli.add_command(sync)
cli.add_command(huginn)
cli.add_command(muninn)
cli.add_command(paths)
cli.add_command(perch)
cli.add_command(spawn)
cli.add_command(merge)
cli.add_command(awaken)

if __name__ == "__main__":
    cli()
