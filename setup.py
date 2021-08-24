#!/usr/bin/env python
import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'thty'
DESCRIPTION = 'Large-scale model example'
URL = ''
EMAIL = 'brianfornelli@gmail.com'
AUTHOR = 'brianfornelli@gmail.com'
REQUIRES_PYTHON = '>=3.6'

VERSION = '1.0.0'

REQUIRED = ["pyspark>=0.2.4", "numpy", "pandas", "scipy", "tiramisu", "bidarka", "lightgbm", "sklearn"]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license='Proprietary',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux'
    ],
    entry_points={
        'console_scripts': [
            'THTY=thty.cli:main'
        ]
    }
)
