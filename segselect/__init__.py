"""Init for seg-select."""

import click

from segselect.commands import select_by_voxel_cli


@click.group()
def segselect():
    """seg-select."""
    segselect.add_command(select_by_voxel_cli)
