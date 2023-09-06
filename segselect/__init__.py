import click

from segselect.commands import select_by_voxel_cli


@click.group()
def segselect():
    segselect.add_command(select_by_voxel_cli)
