import mrcfile
import click
import numpy as np

from pathlib import Path


@click.command()
@click.argument('input_file', nargs=1, type=click.File())
@click.argument('seg_nr', nargs=-1, type=int)
def select_by_voxel_cli(input_file, seg_nr):
    """
    seg-select

    Select specific connected component from segmentation.

    input_file: mrc with component number as voxel value

    seg_nr: voxel value(s) to select.

    output: binary mrc with only all selected voxels set to 1

    """
    select_by_voxel(input_file, seg_nr)


def select_by_voxel(input_file, seg_nr):
    
    input_file = Path(input_file)

    with mrcfile.open(input_file, mode='r') as mrc:
        input_seg = mrc.data
        angpix = mrc.voxel_size.x

    output_seg = np.zeros(input_seg.shape, dtype=np.int8)

    for seg in seg_nr:
        seg = int(seg)
        output_seg[np.where(input_seg == seg)] = 1

    seg_str = [str(seg) for seg in seg_nr]

    mrcfile.write(input_file.with_name(f'{input_file.stem}_sel_{"_".join(seg_str)}.mrc'),
                  data=output_seg, overwrite=True, voxel_size=angpix)

    return input_file.with_name(f'{input_file.stem}_sel_{"_".join(seg_str)}.mrc')
