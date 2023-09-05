import click

from segselect.commands import select


@click.group()
def segselect():
    segselect.add_command(select)
