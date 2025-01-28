# seg-select
Turn voxel-segmentations to binary based on voxel value: All voxels with these values will be set to 1, all others to 0. Will output a mrc file. 

I use this to clean up segmentations from membrain-seg (with ``--store-connected-components``)

Usage: ``segselect segmentation.mrc component1 component2 [...]``

Installation:
`pip install 'git+https://github.com/bwmr/seg-select.git'`