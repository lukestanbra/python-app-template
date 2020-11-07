#!/usr/bin/python3
from setuptools import find_packages, setup
from glob import glob
from os.path import basename, splitext

setup(
    name="hello_world",
    version="1.0.0",
    description="",
    long_description="",
    author="Luke Stanbra",
    author_email="luke.stanbra@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    options={"bdist_wheel": {"universal": True}},
    entry_points={
        'console_scripts': [
            'hello_world = package.cli:main',
        ]
    },
    classifiers = ['Programming Language :: Python :: 3.8'],
    python_requires='>=3.4'
)