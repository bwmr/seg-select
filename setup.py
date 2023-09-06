from setuptools import setup

setup(
    name="segselect",
    version="0.1",
    packages=['segselect'],
    install_requires=[
        'mrcfile',
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'segselect = segselect:select_by_voxel_cli',
        ],
    },
    python_requires=">=3.9",
    author="bwmr",
    description="Write binary segmentation by selecting voxel values.",
    url="https://github.com/bwmr/seg-select"
)
